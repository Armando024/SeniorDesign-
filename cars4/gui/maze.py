#!/usr/bin/python3
import numpy
import pygame as sc
from numpy.random import random_integers as rand
from gui.states import States
from gui.car import Car
from gui.BaseMaze import BaseMaze
from gui.logger import Logger
import ml.predict as predict


DRIVABLE = {0, 2, 3}

class Maze:
    def __init__(self,w=20,h=20,complexity=.75,density=.75, outputfile="out.csv"):
        sc.init()
        self.font=sc.font.SysFont(None ,24 )
        self.text=self.font.render("Right key:changes maze",True,(0,128,0))
        self.text1=self.font.render("Down Key: Increases Density",True,(0,128,0))
        self.text2=self.font.render("Up Key:Increases complexity",True,(0,128,0))
        self.car=Car(4,4,9,9) 
        States.__init__(self)
        self.w=w
        self.h=h

         
        self.maze=BaseMaze(self.w,self.h,complexity,density,1,1,self.w-2,self.h-2)
        self.logger = Logger(open("output/"+outputfile, "w"), self);
        self.predictor = predict.Predictor()

    def get_event(self,event):
        if event.type == sc.KEYDOWN:

            self.logger.log(event.key)

            if event.key==sc.K_RIGHT: #re-builds maze
                self.car=Car(4,4,9,9)
                self.maze.re_Construct()                 
            elif event.key==sc.K_UP: #increases complexity
                self.car=Car(4,4,9,9)
                self.maze.inc_com() 
            elif event.key==sc.K_DOWN: #increases density
                self.car=Car(4,4,9,9)
                self.maze.inc_den()   
            #adding new part to the code

            if event.key==sc.K_a and self.maze.get_Value(int(self.car.get_x()),int(self.car.get_y())-2) in DRIVABLE and self.maze.get_Value(int(self.car.get_x()+1),int(self.car.get_y())-2) in DRIVABLE: #left
                self.car.m_u()
            if event.key==sc.K_d and self.maze.get_Value(int(self.car.get_x()),int(self.car.get_y())+1) in DRIVABLE and self.maze.get_Value(int(self.car.get_x()+1),int(self.car.get_y())+1) in DRIVABLE: #right
                self.car.m_d()
            if event.key==sc.K_w and self.maze.get_Value(int(self.car.get_x())-1,int(self.car.get_y())) in DRIVABLE and self.maze.get_Value(int(self.car.get_x())-1,int(self.car.get_y()-1)) in DRIVABLE: #UP
                self.car.m_l()
            if event.key==sc.K_s and self.maze.get_Value(int(self.car.get_x())+1+1,int(self.car.get_y()-1)) in DRIVABLE and self.maze.get_Value(int(self.car.get_x())+1+1,int(self.car.get_y())) in DRIVABLE: #down
                self.car.m_r()
            # Check whether car has hit the finish
            if self.maze.get_Value(int(self.car.get_x()),int(self.car.get_y())) == 3:
                print("Congratulations!")



    def update(self,screen,dt): 
        self.draw(screen)

        subMaze = predict.subArray(self.maze.maze,self.car.get_x(), self.car.get_y(),24,24)
        # comment below this to not have the bot running
        self.bot_input(self.predictor.act(subMaze))


    def bot_input(self,event):
       
        if event == 1 and self.maze.get_Value(int(self.car.get_x()),int(self.car.get_y())-2) in DRIVABLE and self.maze.get_Value(int(self.car.get_x()+1),int(self.car.get_y())-2) in DRIVABLE: #left
            self.car.m_u()
        if event== 3 and self.maze.get_Value(int(self.car.get_x()),int(self.car.get_y())+1) in DRIVABLE and self.maze.get_Value(int(self.car.get_x()+1),int(self.car.get_y())+1) in DRIVABLE: #right
            self.car.m_d()
        if event== 0 and self.maze.get_Value(int(self.car.get_x())-1,int(self.car.get_y())) in DRIVABLE and self.maze.get_Value(int(self.car.get_x())-1,int(self.car.get_y()-1)) in DRIVABLE: #UP
            self.car.m_l()
        if event == 2 and self.maze.get_Value(int(self.car.get_x())+1+1,int(self.car.get_y()-1)) in DRIVABLE and self.maze.get_Value(int(self.car.get_x())+1+1,int(self.car.get_y())) in DRIVABLE: #down
            self.car.m_r()
        # Check whether car has hit the finish
        if self.maze.get_Value(int(self.car.get_x()),int(self.car.get_y())) == 3:
            print("Congratulations!")



    def draw(self,screen): #actual drawing goes here
        screen.fill((255,255,255)) 
        sc.draw.rect(screen,(130,82,1),sc.Rect(0,0,850,455))
        x1=0
        y1=0
        Cw=4 #cell width
        for a in range(0,self.maze.g_w()):
            for b in range(0,self.maze.g_h()):
                if self.maze.get_Value(b,a)==0: #road
                    sc.draw.rect(screen,(128,128,128),sc.Rect(y1,x1,Cw,Cw))
                    sc.draw.rect(screen,(128,128,128),sc.Rect(y1,x1,Cw,Cw))
                if self.maze.get_Value(b,a)==2: #start
                    sc.draw.rect(screen,(0,0,0),sc.Rect(y1,x1,Cw,Cw))
                    sc.draw.rect(screen,(0,0,0),sc.Rect(y1,x1,Cw,Cw))
                if self.maze.get_Value(b,a)==3: #end
                    sc.draw.rect(screen,(255,255,255),sc.Rect(y1,x1,Cw,Cw))
                    sc.draw.rect(screen,(255,255,255),sc.Rect(y1,x1,Cw,Cw))
                x1=x1+Cw
            y1=y1+Cw
            x1=0

        self.car.draw(screen)
        
        screen.blit(self.text,(0,455))
        screen.blit(self.text1,(0,505))
        screen.blit(self.text2,(0,480))
        screen.blit(self.font.render(( str(round(self.maze.g_com(),2))),True,(0,128,0)),(250,480))
        screen.blit(self.font.render((str(round(self.maze.g_den(),2))),True,(0,128,0)),(250,505))

        return 
    def cleanup(self):
        #createclean up
        pass





