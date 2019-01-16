# _*_ coding: utf-8 _*_

import pygame
from pygame.locals import *
from random import sample

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Mac-mare: help me out !")


def board():
    """Creation of the labyrinth. """
    bg = pygame.image.load("./ressource/floor_lab.png").convert()
    flag = pygame.image.load("./ressource/flag.png").convert()
    mac = pygame.image.load("./ressource/mac_20.png").convert_alpha()

    screen.blit(bg, (0, 0))
    screen.blit(flag, (0, 0))
    screen.blit(mac, (20, 0))
    pygame.display.flip()

def wall():
    """ Creation of the obstacles inside the labyrinth. """
    wall = pygame.image.load("./ressource/wall.png").convert()
# Creating random positions for the obstacles 'wall' on the board game. """
    for x in sample(range(0, 300, 20), k=8):  # choose k random value from the range of possible x values
        for y in sample(range(0, 300), k=5):  # choose k random value from the range of possible y values
            if x <= 20 and y == 0:  # prevent wall from being placed on the start flag and Mac picture
                continue
            if x >= 260 and y == 280:
                continue
            else:
                wall_rect = wall.get_rect()
                screen.blit(wall, wall_rect.move(x, y))
    pygame.display.flip()
    keep = 1
    while keep:
        for event in pygame.event.get():
            if event.type == QUIT:
                keep = 0


if __name__ == "__main__":
    board()
    wall()