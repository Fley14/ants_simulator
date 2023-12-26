import Ants
import pygame
import random as rd
import math


pygame.init()
screen = pygame.display.set_mode((800,800))

nest = Ants.Nest(400,400)

ants_table = []
for i in range(100):
    ants_table.append(Ants.Ant(400,400,(rd.random()*2-1)*math.pi,nest,rd.randint(10,50)))


def go():
    for ant in ants_table:
        if ant.in_nest==0:
            ant.move()
            ant.turn()
            ant.show(screen)
            # ant.trace_nest_dir(screen)
            # ant.nest_return()
            # ant.trace_direction(screen)
            ant.contact_nest()


for i in range(400):
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (400,400,5,5))
    print(i)
    go()
    pygame.display.update()
    pygame.time.delay(50)
    if i%30==0:
        for ant in ants_table:
            ant.nest_return()
    if i==100:
        for ant in ants_table:
            ant.food_find=1


pygame.time.delay(1000)
pygame.quit()

