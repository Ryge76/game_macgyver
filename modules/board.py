# _*_ coding: utf-8 _*_
import pygame
from random import randrange, sample


# Setting display
screen = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Mac-mare: help me out !")

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
        bg = pygame.image.load("./ressource/floor_lab.png").convert()  # background picture
        flag = pygame.image.load("./ressource/flag.png").convert()  # starting point picture
        screen.blit(bg, (20, 20))
        screen.blit(flag, (20, 20))

        door = pygame.image.load("./ressource/exitb.png").convert_alpha()  # ending point picture
        door_rect = door.get_rect()
        door_rect = door_rect.move(280, 280)
        screen.blit(door, door_rect)
        garded.append(door_rect)  # adding the door rectangle to the garded list for interactions

        murdock = pygame.image.load("./ressource/Gardien.png").convert_alpha()
        murdock_rect = murdock.get_rect()
        murdock_rect = murdock_rect.move(250, 260)
        screen.blit(murdock, murdock_rect)
        garded.append(murdock_rect)  # adding the guard rectangle to the garded list for interactions

        pygame.display.flip()
        return garded

    @staticmethod
    def walls():
        """ Creation of the obstacles inside the labyrinth. """
        wall = pygame.image.load("./ressource/wall.png").convert()
        # Creating random positions for the obstacles 'wall' on the board game. """
        for x in sample(range(45, 300, 22), k=8):  # choose k random value from the range of possible x values
            for y in sample(range(20, 260, 22), k=6):  # choose k random value from the range of possible y values
                if x <= 60 and y == 20:  # prevent wall from being placed on the start flag and Mac picture
                    continue
                if x >= 240 and y >= 260:  # prevent walls from being placed on the finish zone.
                    continue
                else:
                    wall_rect = wall.get_rect()
                    wall_rect = wall_rect.move(x, y)
                    screen.blit(wall, wall_rect)
                    obstacles.append(wall_rect)

        pygame.display.flip()

    @staticmethod
    def borders():
        """Creation of 'invisible' borders to prevent the character from leaving the game's board . """
        global obstacles
        wall = pygame.image.load("./ressource/wall.png")
        for x in [0, 300]:  # create left and right side borders of the game
            for y in range(0, 320, 20):
                wall_rect = wall.get_rect()
                wall_rect = wall_rect.move(x, y)
                screen.blit(wall, wall_rect)
                obstacles.append(wall_rect)
        pygame.display.flip()

        for y in [0, 300]:  # create superior and inferior borders of the game
            for x in range(0, 300, 20):
                wall_rect = wall.get_rect()
                wall_rect = wall_rect.move(x, y)
                screen.blit(wall, wall_rect)
                obstacles.append(wall_rect)

        pygame.display.flip()
        return obstacles

    @staticmethod
    def objects():
        """Randomly place the 3 objects to be collected on the board game. """
        global collection
        obj_pic = list()  # will contain the pictures of the objects
        tube = pygame.image.load("./ressource/tube_20.png")  # .convert_alpha()
        needle = pygame.image.load("./ressource/seringue_30.jpg")  # .convert_alpha()
        bottle = pygame.image.load("./ressource/ether_20.png")  # .convert_alpha()

        tube_rect = tube.get_rect()
        obj_pic.append(tube)
        collection.append(tube_rect)  # objects added to collection list for interactions

        needle_rect = needle.get_rect()
        obj_pic.append(needle)
        collection.append(needle_rect)

        bottle_rect = bottle.get_rect()
        obj_pic.append(bottle)
        collection.append(bottle_rect)

        i = 0
        while i <= 2:
            # choosing x and y so the objects are not placed on the start and finish zone
            x = randrange(60, 300, 30)
            y = randrange(60, 260, 20)
            # setting the objects so they don't overlap the walls and the gard
            if collection[i].move(x, y).collidelist(obstacles) == -1 and collection[i].move(x, y).collidelist(
                    garded) == -1 \
                    and collection[i].move(x, y).collidelist(collection) == -1:
                collection[i] = collection[i].move(x, y)
                screen.blit(obj_pic[i], collection[i])
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
        myfont = pygame.font.SysFont("monospace", 15, bold=1)
        myfont2 = pygame.font.SysFont("monospace", 14, bold=1)

        score_dis1 = myfont.render("OBJETS COLLECTES: ", 1, (255, 255, 255))
        score_dis2 = myfont.render(text, 1, (0, 0, 0))
        score_dis3 = myfont.render(" / 3 ", 1, (255, 255, 255))
        esc = myfont2.render("Hit ESCAPE to end game.", 1, (255, 255, 255))
        BoardSetup.borders()
        screen.blit(score_dis1, (50, 300))
        screen.blit(score_dis2, (210, 300))
        screen.blit(score_dis3, (220, 300))
        screen.blit(esc, (120, 2))
        pygame.display.flip()

        return collected

