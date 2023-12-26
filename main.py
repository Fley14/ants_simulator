import Ants
import pygame
import random as rd
import math

screen_width=1300
screen_height=1000

game_go=1
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))

nest = Ants.Nest(400,400,500)

def actualise_go():
    global game_go
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_go=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_go=0

def creat_food(nb):
    food_tab=[]
    for _ in range(nb):
        food_tab.append(Ants.Food(rd.randint(0,screen_width),rd.randint(0,screen_height)))
    return food_tab
def show_food(food_tab):
    for food in food_tab:
        food.show(screen)

food_tab=creat_food(50)
while not nest.all_ant_in_nest() and game_go:
    screen.fill((0,0,0))
    nest.move()
    nest.show(screen)
    show_food(food_tab)
    nest.contact_food(food_tab)
    pygame.display.update()
    pygame.time.delay(10)
    actualise_go()


pygame.quit()

