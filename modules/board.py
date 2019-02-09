# _*_ coding: utf-8 _*_
import pygame
from random import randrange, sample
from modules.constants import *

# lists of rectangles for the obstacles, objects to collect, the final door exit and Murdock the guardian
obstacles = list()
collection = list()
garded = list()

# number of collected objects
collected = 0


class BoardSetup():
    """ Set various elements of the game board: background, walls, borders, objects, score display, etc."""
    @staticmethod
    def board():
        """Creation of the labyrinth board game. """
        global garded

        SCREEN.blit(BG, (20, 20))  # background picture
        SCREEN.blit(FLAG, (20, 20))  # starting point picture

        door_rect = DOOR.get_rect()
        door_rect = door_rect.move(280, 280)
        SCREEN.blit(DOOR, door_rect)  # ending point picture
        garded.append(door_rect)  # adding the door rectangle to the garded list for interactions

        murdoc_rect = MURDOC.get_rect()
        murdoc_rect = murdoc_rect.move(250, 260)
        SCREEN.blit(MURDOC, murdoc_rect)  # guard picture
        garded.append(murdoc_rect)  # adding the guard rectangle to the garded list for interactions

        pygame.display.flip()
        return garded

    @staticmethod
    def walls():
        """ Creation of the obstacles inside the labyrinth. """

        # Creating random positions for the obstacles 'wall' on the board game. """
        for x in sample(range(45, 300, 22), k=8):  # choose k random value from the range of possible x values
            for y in sample(range(20, 260, 22), k=6):  # choose k random value from the range of possible y values
                if x <= 60 and y == 20:  # prevent wall from being placed on the start flag and Mac picture
                    continue
                if x >= 240 and y >= 260:  # prevent walls from being placed on the finish zone.
                    continue
                else:
                    wall_rect = WALL.get_rect()
                    wall_rect = wall_rect.move(x, y)
                    SCREEN.blit(WALL, wall_rect)
                    obstacles.append(wall_rect)

        pygame.display.flip()

    @staticmethod
    def borders():
        """Creation of 'invisible' borders to prevent the character from leaving the game's board . """
        global obstacles

        for x in [0, 300]:  # create left and right side borders of the game
            for y in range(0, 320, 20):
                wall_rect = WALL.get_rect()
                wall_rect = wall_rect.move(x, y)
                SCREEN.blit(WALL, wall_rect)
                obstacles.append(wall_rect)
        pygame.display.flip()

        for y in [0, 300]:  # create superior and inferior borders of the game
            for x in range(0, 300, 20):
                wall_rect = WALL.get_rect()
                wall_rect = wall_rect.move(x, y)
                SCREEN.blit(WALL, wall_rect)
                obstacles.append(wall_rect)

        pygame.display.flip()
        return obstacles

    @staticmethod
    def objects():
        """Randomly place the 3 objects to be collected on the board game. """
        # global collection
        obj_pic = list()  # will contain the pictures of the objects

        tube_rect = TUBE.get_rect()
        obj_pic.append(TUBE)
        collection.append(tube_rect)  # objects added to collection list for interactions

        needle_rect = NEEDLE.get_rect()
        obj_pic.append(NEEDLE)
        collection.append(needle_rect)

        bottle_rect = BOTTLE.get_rect()
        obj_pic.append(BOTTLE)
        collection.append(bottle_rect)

        i = 0
        while i <= 2:
            # choosing x and y so the objects are not placed on the start and finish zone
            x = randrange(60, 300, 30)
            y = randrange(60, 260, 20)
            # setting the objects so they don't overlap the walls, the guard, and other objects
            if collection[i].move(x, y).collidelist(obstacles) == -1 and collection[i].move(x, y).collidelist(
                    garded) == -1 \
                    and collection[i].move(x, y).collidelist(collection) == -1:
                collection[i] = collection[i].move(x, y)
                SCREEN.blit(obj_pic[i], collection[i])
                i += 1
            else:
                continue

        pygame.display.flip()

        return collection

    @staticmethod
    def score(value=0):
        """Count and indicate the number of objects collected in text. """
        global collected
        if value == 0:
            collected = 0
        else:
            collected += value

        # display the text of the number of collected objects.
        text = str(collected)

        score_dis1 = BoardSetup.text("OBJETS COLLECTES: ", 15)
        score_dis2 = BoardSetup.text(text, 15, (0, 0, 0))
        score_dis3 = BoardSetup.text(" / 3 ", 15)
        esc = BoardSetup.text("Hit ESCAPE to end game.", 14)
        BoardSetup.borders()

        SCREEN.blit(score_dis1, (50, 300))
        SCREEN.blit(score_dis2, (210, 300))
        SCREEN.blit(score_dis3, (220, 300))
        SCREEN.blit(esc, (120, 2))
        pygame.display.flip()

        return collected

    @staticmethod
    def text(message, size, color=(255, 255, 255)):
        # default color  = white
        myfont = pygame.font.SysFont("monospace", size, bold=1)
        mytext = myfont.render(message, 1, color)

        return mytext





