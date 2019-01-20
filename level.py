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
garded = list()

# initial copy of the screen. Will contain later on a copy of the full board with obstacles etc. to refresh the \
# background.
screenshot = screen.copy()


def board():
    """Creation of the labyrinth board game. """
    global garded, bg
    bg = pygame.image.load("./ressource/floor_lab.png").convert()
    flag = pygame.image.load("./ressource/flag.png").convert()

    screen.blit(bg, (0, 0))
    screen.blit(flag, (0, 0))

    door = pygame.image.load("./ressource/exitb.png").convert_alpha()
    door_rect = door.get_rect()
    door_rect = door_rect.move(280, 280)
    screen.blit(door, door_rect)
    garded.append(door_rect)  # adding the door rectangle to the leave list for interactions

    murdock = pygame.image.load("./ressource/Gardien.png").convert_alpha()
    murdock_rect = murdock.get_rect()
    murdock_rect = murdock_rect.move(240, 260)
    screen.blit(murdock, murdock_rect)
    garded.append(murdock_rect)  # adding the guard rectangle to the keeper list for interactions

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


def walls():
    """ Creation of the obstacles inside the labyrinth. """
    wall = pygame.image.load("./ressource/wall.png").convert()
# Creating random positions for the obstacles 'wall' on the board game. """
    for x in sample(range(0, 300, 22), k=8):  # choose k random value from the range of possible x values
        for y in sample(range(0, 300, 22), k=5):  # choose k random value from the range of possible y values
            if x <= 30 and y == 0:  # prevent wall from being placed on the start flag and Mac picture
                continue
            if x >= 240 and y >= 260:  # prevent walls from being placed on the finish zone.
                continue
            else:
                wall_rect = wall.get_rect()
                wall_rect = wall_rect.move(x, y)
                screen.blit(wall, wall_rect)
                obstacles.append(wall_rect)

    pygame.display.flip()


def objects():
    """Randomly place the 3 objects to be collected on the board game. """
    global collection, screenshot
    obj_pic = list()  # will contain the pictures of the objects
    tube = pygame.image.load("./ressource/tube_20.png").convert_alpha()
    needle = pygame.image.load("./ressource/seringue_30.jpg").convert_alpha()
    bottle = pygame.image.load("./ressource/ether_20.png").convert_alpha()

    tube_rect = tube.get_rect()
    obj_pic.append(tube)
    collection.append(tube_rect)

    needle_rect = needle.get_rect()
    obj_pic.append(needle)
    collection.append(needle_rect)

    bottle_rect = bottle.get_rect()
    obj_pic.append(bottle)
    collection.append(bottle_rect)

    i=0
    while i <= 2:
        # choosing x and y so the objects are not placed on the start and finish zone
        x = randrange(40, 260, 30)
        y = randrange(20, 260, 20)
        # setting the objects so they don't overlap the walls and the gard
        if collection[i].move(x, y).collidelist(obstacles) == -1 and collection[i].move(x, y).collidelist(garded) == -1 \
                and collection[i].move(x, y).collidelist(collection) == -1:
            collection[i] = collection[i].move(x, y)
            screen.blit(obj_pic[i], collection[i])
            i += 1
        else:
            continue

    pygame.display.flip()
    screenshot = screen.copy()  # copy of the completed background.


def player():
    global mac, mac_rect
    mac = pygame.image.load("./ressource/mac_20.png").convert_alpha()
    mac_rect = mac.get_rect()
    mac_rect = mac_rect.move(20, 0)
    screen.blit(mac, mac_rect)
    pygame.display.flip()


def ambiance():
    """ Create musical ambiance of the game. """
    global ring, shout, clap
    pygame.mixer.music.load("./ressource/ambiance2.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    pygame.mixer.music.queue("./ressource/ambiance.ogg")
# sound effects
    ring = pygame.mixer.Sound("./ressource/sonnette_velo.ogg")
    shout = pygame.mixer.Sound("./ressource/cri.ogg")
    clap = pygame.mixer.Sound("./ressource/bravo.ogg")


def wined():
    win = pygame.image.load("./ressource/win_MG.jpg")
    # message to display
    myfont = pygame.font.SysFont("monospace", 28, bold=1)
    lm = myfont.render("Yess ! I'm free !!", 1, (117, 22, 11))
    lm2 = myfont.render("So long Murdoc !!", 1, (117, 22, 11))
    screen.blit(bg, (0, 0))
    screen.blit(win, (25, 40))
    screen.blit(lm, (10, 10))
    screen.blit(lm2, (30, 270))
    pygame.display.flip()
    pygame.time.wait(12000)

    garded[:], collection[:], obstacles[:] = [], [], []
    start()


def failed():
    fail = pygame.image.load("./ressource/fail_Murdoc.jpg")
    # message to display
    myfont = pygame.font.SysFont("monospace", 28, bold=1)
    lm = myfont.render("I finally got you",  1, (117, 22, 11))
    lm2 = myfont.render("MacGyver !!", 1, (117, 22, 11))
    screen.blit(bg, (0, 0))
    screen.blit(fail, (25, 55))
    screen.blit(lm, (10, 10))
    screen.blit(lm2, (70, 250))
    pygame.display.flip()
    pygame.time.wait(3000)

    garded[:], collection[:], obstacles[:] = [], [], []
    start()


def start():
    board()
    borders()
    walls()
    objects()
    player()
    ambiance()

    global mac_rect, mac, screenshot
    collected = 0
    mask = pygame.image.load("./ressource/floor_mask2.png").convert()  # image to mask the collected objects
    death = pygame.image.load("./ressource/mort.png")  # image of failed mission
    # death_rect = death.get_rect()

    pygame.key.set_repeat(10, 30)  # set the repeat function for the keyboard

    keep = 1
    while keep:
        if mac_rect.collidelist(collection) != -1:
            ring.play()
            collected += 1
            index = mac_rect.collidelist(collection)
            screen.blit(mask, mac_rect)  # remove Mac picture for the board
            screen.blit(mask, collection[index])  # hide the object
            del collection[index]
            pygame.display.flip()
            screenshot = screen.copy()  # update the background with a scene without the object
            screen.blit(mac, mac_rect)
            pygame.display.flip()


        if mac_rect.collidelist(garded) != -1:
            if collected < 3:
                # sound effects
                pygame.mixer.music.pause()
                shout.play()
                # replace Mac pic with a skeleton
                screen.blit(mask, mac_rect)
                screen.blit(death, mac_rect)
                pygame.display.flip()

                pygame.time.wait(2000)
                collected = 0  # set back to 0 for new game
                failed()

            else:
                clap.play()
                pygame.mixer.music.fadeout(1000)

                wined()

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
    start()

