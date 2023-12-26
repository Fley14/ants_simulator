import Ants
import pygame
import random as rd
import math

game_go=1
pygame.init()
screen = pygame.display.set_mode((800,800))

nest = Ants.Nest(400,400,100)

def actualise_go():
    global game_go
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_go=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_go=0
i=0
while not nest.all_ant_in_nest() and game_go and i<1000:
    screen.fill((0,0,0))
    i+=1
    nest.move()
    nest.show(screen)
    pygame.display.update()
    pygame.time.delay(10)
    actualise_go()


pygame.time.delay(1000)
pygame.quit()

