# _*_ coding: utf-8 _*_
import pygame
from pygame.locals import *
import modules.board

# Setting display
screen = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Mac-mare: help me out !")

# background for the board
bg = pygame.image.load("./ressource/floor_lab.png").convert()


class Player():
    """Functions related to the player: picture, animation, success/failure screen, game's rules. """
    @staticmethod
    def player():
        """Create MacGyver player on the board and rectangle to animate him. """
        global mac, mac_rect
        mac = pygame.image.load("./ressource/mac_20.png").convert_alpha()
        mac_rect = mac.get_rect()
        mac_rect = mac_rect.move(20, 20)
        screen.blit(mac, mac_rect)
        pygame.display.flip()
        return mac, mac_rect

    @staticmethod
    def intro():
        """Display initial splash screen. """

        screen.fill((0, 0, 0))
        intro = pygame.image.load("./ressource/intro_MG.jpg")
        screen.blit(intro, (0, 45))
        pygame.display.flip()

        # introduction music
        pygame.mixer.music.load("./ressource/heart.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=4)
        pygame.time.wait(2000)
        Player.explain()

    @staticmethod
    def explain():
        """ display the game's rules """

        myfont = pygame.font.SysFont("monospace", 15, bold=1)
        exp1 = myfont.render("Help MacGyver escape the labyrinth.", 1, (255, 255, 255))
        exp2 = myfont.render("Alive... ;-)", 1, (255, 0, 0))
        exp3 = myfont.render("For that you will need 3 objects.", 1, (255, 255, 255))
        exp4 = myfont.render("Find them and get rid of Murdoc !", 1, (255, 255, 255))
        exp5 = myfont.render("Use ARROW KEYS to move.", 1, (255, 255, 0))
        exp6 = myfont.render("Press ENTER to stop the music.", 1, (255, 255, 0))
        exp9 = myfont.render("Press SPACE to resume the music.", 1, (255, 255, 0))
        exp7 = myfont.render("During the game: ", 1, (255, 255, 0))
        exp8 = myfont.render("Ready ? ==> Press F1 to start !", 1, (0, 255, 0))
        exp11 = myfont.render("Afraid ? ==> Press ESCAPE to quit...", 1, (255, 0, 0))
        exp10 = myfont.render("Press ESCAPE to exit game.", 1, (255, 255, 0))

        # list of message to display
        show = [exp1, exp2, exp3, exp4, exp7, exp5, exp6, exp9, exp10, exp8, exp11]

        # animation of the messages
        screen.fill((0, 0, 0))
        n = 10  # needed to increment y value
        for index in range(4):
            screen.blit(show[index], (5, index * 11 + n))
            n *= 1.25
        pygame.display.flip()

        n = 40  # needed to increment y value
        for index in range(4, 11):
            screen.blit(show[index], (5, index * 12 + n))
            n *= 1.25
        pygame.display.flip()

        # get keyboard input to start or leave the game
        keep = 1
        while keep:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_F1:
                        keep = 0
                        # start()
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()

    @staticmethod
    def winned():
        """Display the success screen. """
        win = pygame.image.load("./ressource/win_MG.jpg")

        # message to display
        myfont = pygame.font.SysFont("monospace", 28, bold=1)
        lm = myfont.render("Yess ! I'm free !", 1, (242, 202, 0))
        lm2 = myfont.render("So long Murdoc !", 1, (242, 202, 0))

        modules.board.BoardSetup.borders()  # refresh the borders to erase the score text
        screen.blit(bg, (10, 10))
        screen.blit(win, (25, 40))
        screen.blit(lm, (20, 10))
        screen.blit(lm2, (30, 280))

        pygame.display.flip()
        pygame.time.wait(12000)

    @staticmethod
    def failed():
        """Display the game over screen. """
        fail = pygame.image.load("./ressource/fail_Murdoc.jpg")

        # message to display
        myfont = pygame.font.SysFont("monospace", 28, bold=1)
        lm = myfont.render("I finally got you",  1, (117, 22, 11))
        lm2 = myfont.render("MacGyver !!", 1, (117, 22, 11))

        modules.board.BoardSetup.borders()  # refresh the borders to erase the score text
        screen.blit(bg, (10, 10))
        screen.blit(fail, (25, 55))
        screen.blit(lm, (10, 10))
        screen.blit(lm2, (70, 250))

        pygame.display.flip()
        pygame.time.wait(3000)
