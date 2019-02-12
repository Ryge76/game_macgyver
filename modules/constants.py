import pygame

"""Contains the constants of the game. """
# screen parameters
WIDTH = 320
HEIGHT = 320

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mac-mare: help me out !")

# game's elements pictures

# background picture
BG = pygame.image.load("./ressource/floor_lab.png").convert()
# starting point picture
FLAG = pygame.image.load("./ressource/flag.png").convert()
# ending point picture
DOOR = pygame.image.load("./ressource/exitb.png").convert_alpha()
WALL = pygame.image.load("./ressource/wall.png").convert()
TUBE = pygame.image.load("./ressource/tube_20.png")
NEEDLE = pygame.image.load("./ressource/seringue_30.jpg")
BOTTLE = pygame.image.load("./ressource/ether_20.png")
# image to mask the collected objects
MASK = pygame.image.load("./ressource/floor_mask2.png").convert()
# image of failed mission replacing the main character picture
DEATH = pygame.image.load("./ressource/mort.png")

# guard picture
MURDOC = pygame.image.load("./ressource/Gardien.png").convert_alpha()
# main character picture
MAC = pygame.image.load("./ressource/mac_20.png").convert_alpha()

# introduction splash screen picture
INTRO = pygame.image.load("./ressource/intro_MG.jpg")
# victory picture
WIN = pygame.image.load("./ressource/win_MG.jpg")
