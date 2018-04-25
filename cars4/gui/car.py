#!/usr/bin/python

class Car:
    def __init__(self, w=5,h=5,x=0,y=0):
        self.w=w
        self.h=h
        self.x=x
        self.y=y
        self.temp_sides=0
        self.up_down=0
       # self.first_time=True
         #the multi used for gui
    def __str__(self):
        #for debuffing puposes
        temp="x=="+str(self.x)+" y=="+str(self.y) + " x_off==" +str(self.temp_sides) + " y_off=="+str(self.up_down) 
        return temp
    def get_x1(self):
        return self.x*(30)+(self.up_down*5)
    def get_y1(self):
        #if self.first_time:
         #   return self.y*30+(self.temp_sides)
        #print(self.y*30+(self.temp_sides*5))
        return self.y*30+(self.temp_sides*5)
    def get_x(self): 
        return self.x
    
    def get_y(self):
        return self.y
    
    def m_r(self): #move right
        if (self.up_down is 6):
            self.x+=1
            self.up_down=0
        self.up_down+=1
        return
    def dec_up_down(self):
        if (self.up_down is not 0 ):
            self.up_down-=1
        return
    def inc_up_down(self):
        if (self.up_down is not 4):
            self.up_down+=1
        return
    def m_l(self): #move left
        if (self.up_down is 0):
            self.x-=1
            self.up_down=6
        self.up_down-=1
        return 
    def dec_side(self):
        if(self.temp_sides is not 0):
            self.temp_sides-=1
        return
    def inc_side(self):
        if(self.temp_sides is not 4):
            self.temp_sides+=1
    def m_u(self): #move real left
        if (self.temp_sides is 0):
            #print("chaging y")
            self.y-=1
            self.temp_sides=6
        #print("chaging sides temp")
        self.temp_sides-=1
        return
    
    def m_d(self): #move real right
       # print("going right") 
        if (self.temp_sides is 6):
            self.y+=1
            self.temp_sides=0
       # self.first_time=False
        self.temp_sides+=1
        return

    def get_w(self): #get the width
        return self.w

    def get_h(self): #get the height
        return self.h 
    
  









