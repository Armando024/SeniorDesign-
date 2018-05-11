#!/usr/bin/python
import pygame as sc
class Car:
    def __init__(self, w=5,h=5,x=0,y=0):
        self.w=w
        self.h=h
        self.x=x #x for first panel
        self.y=y #y for first panel
        self.x1=x
        self.y1=y-1
        self.x2=x+1
        self.y2=y
        self.x3=x+1
        self.y3=y-1
        self.temp_sides=0
        self.up_down=0
    def __str__(self):
        #for debugging puposes
        temp="x=="+self.x+" y=="+self.y
        return temp
  #  def canMove(self,value,direction):
   #     if(direction is 0): #left direction=0  
    #        if(   ):   
     #   return
    def get_x1(self):#my actual y
        return self.x
    def get_y1(self):#my actual corner
        return self.y
    def get_x(self): 
        return self.x
    def get_y(self):
        return self.y
    def draw(self,screen):
        #top right
        sc.draw.rect(screen,(0,0,255),sc.Rect((self.y*4,self.x*4,self.get_h(),self.get_w())))
        #top left
        sc.draw.rect(screen,(0,0,255),sc.Rect((self.y1*4,self.x1*4,self.get_h(),self.get_w())))
        #down right
        sc.draw.rect(screen,(0,0,255),sc.Rect((self.y2*4,self.x2*4,self.get_h(),self.get_w())))
        #down left
        sc.draw.rect(screen,(0,0,255),sc.Rect(((self.y3)*4,self.x3*4,self.get_h(),self.get_w())))
        return
    def m_r(self): #move right
        self.x+=1
        self.x1+=1
        self.x2+=1
        self.x3+=1
        return
    def m_l(self): #move left
        self.x-=1
        self.x1-=1
        self.x2-=1
        self.x3-=1
        return 
    def m_u(self): #move real left
        self.y-=1
        self.y1-=1
        self.y2-=1
        self.y3-=1
        return
    def m_d(self): #move real right
        self.y+=1
        self.y1+=1
        self.y2+=1
        self.y3+=1
        return
    def get_w(self): #get the width
        return self.w
    def get_h(self): #get the height
        return self.h 
