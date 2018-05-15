#!/usr/bin/python3
import numpy
import pygame as sc
from numpy.random import random_integers as rand
from gui.states import States
from gui.pygame_textinput import TextInput
class NameInput:
    def __init__(self):
        sc.init()
        self.font=sc.font.SysFont(None ,35 )
        self.text=self.font.render("Enter File Name:",True,(0,128,0))
   
        States.__init__(self)
        self.mode=0
        self.next='Maze'
        self.textinput=TextInput()
    def get_event(self,event):
        
        if(self.textinput.update(event)):
            #print(self.textinput.get_text())
            self.done=True
    
    def update(self,screen,dt): 
        self.draw(screen)
    def startup(self,data):
        sc.key.set_repeat(1, 500)  
        self.data=data
        return
    def get_data(self):
        a=[]
        a.append(str(2))
        a.append(self.textinput.get_text())
        print("good here")
        return a
    
    def draw(self,screen): #actual drawing goes here
        screen.fill((255,255,255)) 
        #sc.draw.rect(screen,(130,82,1),sc.Rect(0,0,850,455))
        screen.blit(self.text,(150,200))
        screen.blit(self.textinput.get_surface(), (350, 200))
        return 
    def cleanup(self):
        #createclean up
        pass

