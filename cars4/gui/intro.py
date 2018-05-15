#!/usr/bin/python3
import numpy
import pygame as sc
from numpy.random import random_integers as rand
from gui.states import States

class Intro:
    def __init__(self):
        sc.init()
        self.font=sc.font.SysFont(None ,32)
        self.text=self.font.render("Pressed t key to train the bot",True,(0,128,0))
        self.text1=self.font.render("Pressed b key to test the model",True,(0,128,0))
        self.text2=self.font.render("Pressed p key to just play",True,(0,128,0))
        self.carimg=sc.image.load('gui/car.png')
        self.carimg=sc.transform.scale(self.carimg,(263,123))
        States.__init__(self)
        self.mode=0
    def get_event(self,event):
        if event.type == sc.KEYDOWN:
            
            if event.key==sc.K_t: #left 
                print("t key is pressed")
                self.next='FileName'
                self.done=True
                self.mode=2
            if event.key==sc.K_b: #right
                print("b key is pressed")
                self.next='Maze'
                self.done=True
                self.mode=1
            if event.key==sc.K_p: #UP
                print("p key is pressed")
                self.next='Maze'
                self.done=True    
                self.mode=0
    def update(self,screen,dt): 
        self.draw(screen)
    
    def get_data(self):
        a=[]
        a.append(str(self.mode))
        a.append("out.csv")
        return a
    
    def draw(self,screen): #actual drawing goes here
        screen.fill((255,255,255)) 
        #sc.draw.rect(screen,(130,82,1),sc.Rect(0,0,850,455))
       
        screen.blit(self.text,(250,265)) #455
        screen.blit(self.text1,(250,315)) #505
        screen.blit(self.text2,(250,290)) #480
        screen.blit(self.carimg,(260,135))
        return 
    def cleanup(self):
        #createclean up
        pass

