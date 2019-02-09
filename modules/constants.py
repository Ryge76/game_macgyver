import pygame

"""Contains the constants of the game. """
# screen parameters
WIDTH = 320
HEIGHT = 320

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mac-mare: help me out !")

# game's elements pictures
BG = pygame.image.load("./ressource/floor_lab.png").convert()  # background picture
FLAG = pygame.image.load("./ressource/flag.png").convert()  # starting point picture
DOOR = pygame.image.load("./ressource/exitb.png").convert_alpha()  # ending point picture
WALL = pygame.image.load("./ressource/wall.png").convert()
TUBE = pygame.image.load("./ressource/tube_20.png")
NEEDLE = pygame.image.load("./ressource/seringue_30.jpg")
BOTTLE = pygame.image.load("./ressource/ether_20.png")
MASK = pygame.image.load("./ressource/floor_mask2.png").convert()  # image to mask the collected objects
DEATH = pygame.image.load("./ressource/mort.png")  # image of failed mission replacing the main character picture

MURDOC = pygame.image.load("./ressource/Gardien.png").convert_alpha()  # guard picture
MAC = pygame.image.load("./ressource/mac_20.png").convert_alpha()  # main character picture

INTRO = pygame.image.load("./ressource/intro_MG.jpg")  # introduction splash screen picture
WIN = pygame.image.load("./ressource/win_MG.jpg")  # victory picture