import math
import pygame
import random as rd
import numpy as np
debug=0

def angle(vect1,vect2):
    scal=np.dot(vect1,vect2)
    norm_vect1=np.linalg.norm(vect1)
    norm_vect2=np.linalg.norm(vect2)
    cos=scal/(norm_vect1*norm_vect2)
    return math.acos(cos)


class Nest:
    color = (255,0,0)
    def __init__(self,x,y,nb_ant):
        self.rect=pygame.Rect(x,y,10,10)
        self.nb_ant=nb_ant
        self.ants_table=[]
        for i in range(nb_ant):
            self.ants_table.append(Ant(x,y,(rd.random()*2-1)*math.pi,self,rd.randint(1,50)))
    
    def show(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)
        for ant in self.ants_table:
            ant.show(screen)
            if debug:
                ant.trace_nest_dir(screen)
                ant.trace_direction(screen)
    def move(self):
        for ant in self.ants_table:
            ant.move()
            ant.turn()
            ant.contact_nest()
            ant.nest_return()
    
    def all_ant_in_nest(self):
        for ant in self.ants_table:
            if not ant.in_nest:
                return 0
        return 1
    



class Ant:
    width = 5
    length = 5
    color = (255,255,255)
    speed = 1
    
    def __init__(self,x,y,direction,nest,sense_direction):
        """
        this function initialize the ant mith a position and a direction
        the direction is in radiant
        the sens of direction is the capacity of the ant to find the nest more the number is high
          more dificult is for the ant to find the nest
        """
        self.rect=pygame.Rect(x,y,self.width,self.length)
        self.direction = direction
        self.nest_dir=np.array([-math.cos(self.direction),-math.sin(self.direction)],float)
        self.nest_dir%=2*math.pi
        self.nest=nest
        self.sense_direction=sense_direction
        self.food_find =0
        self.in_nest=0
        self.return_nest_count=0


    def move(self):
        if not self.in_nest:
            self.return_nest_count+=1
            addx=math.cos(self.direction)*self.speed
            addy=math.sin(self.direction)*self.speed
            self.rect.x += addx
            self.rect.y += addy
            add = np.array([-addx,-addy],float)
            self.nest_dir=self.nest_dir+add

    def turn(self):
        self.direction += rd.random()-0.5
        self.direction %= 2*math.pi
    
    def show(self,screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def __repr__(self):
        return f'Ant({self.rect.x},{self.rect.y},{self.sense_direction},{self.return_nest_count})'
        
    def nest_return(self):
        if self.food_find==1 and self.return_nest_count>self.sense_direction:
            self.return_nest_count=0
            self.direction=angle(self.nest_dir,np.array([1,0],float))
            if self.rect.y>self.nest.rect.y:
                self.direction*=-1
            self.direction%=2*math.pi

    def trace_nest_dir(self,screen):
        pygame.draw.line(screen, (0,255,0), (self.rect.x,self.rect.y), (self.rect.x+self.nest_dir[0],self.rect.y+self.nest_dir[1]), 1)
    
    def trace_direction(self,screen):
        pygame.draw.line(screen, (255,255,0), (self.rect.x,self.rect.y), (self.rect.x+math.cos(self.direction)*20,self.rect.y+math.sin(self.direction)*20), 1)
        
    def contact_nest(self):
        if self.rect.colliderect(self.nest.rect) and self.food_find==1:
            self.in_nest=1