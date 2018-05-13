import pygame as sc
import sys
from gui.maze import Maze
from gui.states import States
class Controls:
    def __init__(self,size_w=750,size_h=525,fps=60):
        self.done=False
        self.W=size_w
        self.H=size_h
        self.fps=fps
        #settings
        self.window=sc.display.set_mode((self.W,self.H))
        self.clock=sc.time.Clock()
    def setup(self,states,start):
        self.states=states
        self.start_state=start
        self.current_state=self.states[self.start_state]
        
    def state_change(self):
        self.current_state.done=False
        previous,self.start_state=self.start_state,self.current_state.next
        self.current_state.cleanup()
        self.current_state=self.states[self.start_state]
        self.current_state.startup()
        self.current_state.previous=previous
        
    def update(self,temp):
        if self.current_state.quit:
            self.done=True
        elif self.current_state.done:
            print("updating state\n")
            self.state_change()
        self.current_state.update(self.window,temp)
    def event_loop(self):
        for event in sc.event.get():
            if event.type== sc.QUIT:
                self.done=True
            self.current_state.get_event(event)

    def main_loop(self):
        while not self.done:
            timer=self.clock.tick(self.fps)/100.0
            self.event_loop()
            self.update(timer)
            sc.display.update()

if __name__=='__main__':

    outputfile = input("Output File:")
    con,dens = .2,.2
    states={
        'Maze':Maze(25,15,con,dens,outputfile) 
        #add more states ...  50 30
    }
    sc.key.set_repeat(1, 28)   
    app=Controls(800,525,60) #(width of screen,height, frames per second)
    app.setup(states,'Maze')
    app.main_loop()
    sc.quit()
    sys.exit() 








