# _*_ coding: utf-8 _*_

import pygame
from pygame.locals import *
from random import sample, randrange


pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Mac-mare: help me out !")

# lists of rectangles for the obstacles, objects to collect, the final door exit and Murdock the guardian
obstacles = list()
collection = list()
leave = list()
keeper = list()

# initial copy of the screen. Will contain later on a copy of the full board with obstacles etc. to refresh the \
# background.
screenshot = screen.copy()


def board():
    """Creation of the labyrinth board game. """
    global leave, keeper
    bg = pygame.image.load("./ressource/floor_lab.png").convert()
    flag = pygame.image.load("./ressource/flag.png").convert()

    screen.blit(bg, (0, 0))
    screen.blit(flag, (0, 0))

    door = pygame.image.load("./ressource/exitb.png").convert_alpha()
    door_rect = door.get_rect()
    screen.blit(door, door_rect.move(280, 280))
    leave.append(door_rect)  # adding the door rectangle to the leave list for interactions

    murdock = pygame.image.load("./ressource/Gardien.png").convert_alpha()
    murdock_rect = murdock.get_rect()
    screen.blit(murdock, murdock_rect.move(240, 260))
    keeper.append(murdock_rect)  # adding the guard rectangle to the keeper list for interactions

    pygame.display.flip()


def objects():
    global collection
    obj = list()  # will contain the pictures
    tube = pygame.image.load("./ressource/tube_20.png").convert_alpha()
    needle = pygame.image.load("./ressource/needle_30.jpg").convert_alpha()
    bottle = pygame.image.load("./ressource/ether_20.png").convert_alpha()

    tube_rect = tube.get_rect()
    obj.append(tube)
    collection.append(tube_rect)

    needle_rect = needle.get_rect()
    obj.append(needle)
    collection.append(needle_rect)

    bottle_rect = bottle.get_rect()
    obj.append(bottle)
    collection.append(bottle_rect)

    i=0
    while i<=2:
        x = randrange(40, 240, 20)
        y = randrange(20, 260, 20)
        screen.blit(obj[i], collection[i].move(x, y))
        i += 1

    pygame.display.flip()


def borders():
    """Creation of 'invisible' borders to prevent the character from leaving the game's board . """
    global obstacles
    wall = pygame.image.load("./ressource/wall.png")
    for x in [-20, 300]:  # create left and right side borders of the game
        for y in range(-20, 320, 20):
            wall_rect = wall.get_rect()
            wall_rect = wall_rect.move(x, y)
            screen.blit(wall, wall_rect)
            obstacles.append(wall_rect)

    for y in [-20, 300]:  # create up and down borders of the game
        for x in range(0, 300, 20):
            wall_rect = wall.get_rect()
            wall_rect = wall_rect.move(x, y)
            screen.blit(wall, wall_rect)
            obstacles.append(wall_rect)
    pygame.display.flip()


def walls(): # NOT READY YET: walls collide with objects
    """ Creation of the obstacles inside the labyrinth. """
    global screenshot
    wall = pygame.image.load("./ressource/wall.png").convert()
# Creating random positions for the obstacles 'wall' on the board game. """
    for x in sample(range(0, 300, 22), k=8):  # choose k random value from the range of possible x values
        for y in sample(range(0, 300, 22), k=5):  # choose k random value from the range of possible y values
            if x <= 20 and y == 0:  # prevent wall from being placed on the start flag and Mac picture
                continue
            if x >= 240 and y >= 260:  # prevent walls from being placed on the finish zone.
                continue
            else:
                wall_rect = wall.get_rect()
                if wall_rect.move(x, y).collidelist(collection) == -1:
                    wall_rect = wall_rect.move(x, y)
                    screen.blit(wall, wall_rect)
                    obstacles.append(wall_rect)
                else:
                    continue

    pygame.display.flip()
    screenshot = screen.copy()  # copy of the completed background.


def player():
    mac = pygame.image.load("./ressource/mac_20.png").convert_alpha()
    mac_rect = mac.get_rect()
    mac_rect = mac_rect.move(20, 0)
    screen.blit(mac, mac_rect)
    pygame.display.flip()

# Create musical ambiance
    pygame.mixer.music.load("./ressource/ambiance2.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    pygame.mixer.music.queue("./ressource/ambiance.ogg")


# Manage player control with keyboaard
    pygame.key.set_repeat(10, 30) # set the repeat function for the keyboard

    keep = 1
    while keep:
        for event in pygame.event.get():
            if event.type == QUIT:
                keep = 0


            if event.type == KEYDOWN:  # keyboard'controls of Mac and sound animation
                if event.key == K_RETURN:
                    pygame.mixer.music.pause()
                if event.key == K_SPACE:
                    pygame.mixer.music.unpause()

                if event.key == K_UP and mac_rect.move(0, -3).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(0, -3)
                    screen.blit(screenshot, (0, 0))
                    screen.blit(mac, mac_rect)
                    pygame.display.flip()

                if event.key == K_DOWN and mac_rect.move(0, 3).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(0, 3)
                    screen.blit(screenshot, (0, 0))
                    screen.blit(mac, mac_rect)
                    pygame.display.flip()

                if event.key == K_LEFT and mac_rect.move(-3, 0).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(-3, 0)
                    screen.blit(screenshot, (0, 0))
                    screen.blit(mac, mac_rect)
                    pygame.display.flip()

                if event.key == K_RIGHT and mac_rect.move(3, 0).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(3, 0)
                    screen.blit(screenshot, (0, 0))
                    screen.blit(mac, mac_rect)
                    pygame.display.flip()


if __name__ == "__main__":
    board()
    borders()
    objects()
    walls()
    player()

