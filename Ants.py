import math
import pygame
import random as rd
import numpy as np


def angle(vect1,vect2):
    scal=np.dot(vect1,vect2)
    norm_vect1=np.linalg.norm(vect1)
    norm_vect2=np.linalg.norm(vect2)
    cos=scal/(norm_vect1*norm_vect2)
    return math.acos(cos)


class Nest:
    width = 10
    length = 10
    color = (255,0,0)

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self,screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.length))


class Ant:
    rect=pygame.Rect(0,0,5,5)
    color = (255,255,255)
    speed = 1
    food_find =0
    in_nest=0
    return_nest_count=0
    def __init__(self,x,y,direction,nest,sense_direction):
        """
        this function initialize the ant mith a position and a direction
        the direction is in radiant
        the sens of direction is the capacity of the ant to find the nest more the number is high
          more dificult is for the ant to find the nest
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.nest_dir=np.array([-math.cos(self.direction),-math.sin(self.direction)],float)
        self.nest_dir%=2*math.pi
        self.nest=nest
        self.sense_direction=sense_direction
        self.rect.x=x
        self.rect.y=y

    def move(self):
        if not self.in_nest:
            self.return_nest_count+=1
            addx=math.cos(self.direction)*self.speed
            addy=math.sin(self.direction)*self.speed
            self.x += addx
            self.y += addy
            add = np.array([-addx,-addy],float)
            self.nest_dir=self.nest_dir+add

    def turn(self):
        self.direction += rd.random()-0.5
        self.direction %= 2*math.pi
    
    def show(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def __repr__(self):
        return f'Ant({self.x},{self.y},{self.direction},{self.nest_dir})'
        
    def nest_return(self):
        if self.food_find==1 and self.return_nest_count==self.sense_direction:
            self.return_nest_count=0
            self.direction=angle(self.nest_dir,np.array([1,0],float))
            if self.y>self.nest.y:
                self.direction*=-1
            self.direction%=2*math.pi

    def trace_nest_dir(self,screen):
        pygame.draw.line(screen, (0,255,0), (self.x,self.y), (self.x+self.nest_dir[0],self.y+self.nest_dir[1]), 1)
    
    def trace_direction(self,screen):
        pygame.draw.line(screen, (255,255,0), (self.x,self.y), (self.x+math.cos(self.direction)*20,self.y+math.sin(self.direction)*20), 1)
    
    def contact(self,rec):
        if self.x>rec.x and self.x<rec.x+rec.width and self.y>rec.y and self.y<rec.y+rec.length and self.food_find==1:
            return True
        else:
            return False
        
    def contact_nest(self):
        if self.x>self.nest.x and self.x<self.nest.x+self.nest.width and self.y>self.nest.y and self.y<self.nest.y+self.nest.length and self.food_find==1:
            self.in_nest=1
            return True
        else:
            return False