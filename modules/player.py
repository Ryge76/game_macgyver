# _*_ coding: utf-8 _*_
import pygame
from pygame.locals import *
import modules.board as b
from modules.constants import *


class Player():
    """Functions related to the player: picture, animation, success/failure screen, game's rules. """
    @staticmethod
    def player():
        """Create MacGyver player on the board and rectangle to animate him. """

        mac_rect = MAC.get_rect()
        mac_rect = mac_rect.move(20, 20)
        SCREEN.blit(MAC, mac_rect)
        pygame.display.flip()
        return mac_rect

    @staticmethod
    def intro():
        """Display initial splash screen. """

        SCREEN.fill((0, 0, 0))
        SCREEN.blit(INTRO, (0, 45))
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

        exp1 = b.BoardSetup.text("Help MacGyver escape the labyrinth.", 15)
        exp2 = b.BoardSetup.text("Alive... ;-)", 15, (255, 0, 0))
        exp3 = b.BoardSetup.text("For that you will need 3 objects.", 15)
        exp4 = b.BoardSetup.text("Find them and get rid of Murdoc !", 15)
        exp5 = b.BoardSetup.text("Use ARROW KEYS to move.", 15, (255, 255, 0))
        exp6 = b.BoardSetup.text("Press ENTER to stop the music.", 15, (255, 255, 0))
        exp9 = b.BoardSetup.text("Press SPACE to resume the music.", 15, (255, 255, 0))
        exp7 = b.BoardSetup.text("During the game: ", 15, (255, 255, 0))
        exp8 = b.BoardSetup.text("Ready ? ==> Press F1 to start !", 15, (0, 255, 0))
        exp11 = b.BoardSetup.text("Afraid ? ==> Press ESCAPE to quit...", 15, (255, 0, 0))
        exp10 = b.BoardSetup.text("Press ESCAPE to exit game.", 15, (255, 255, 0))

        # list of message to display
        show = [exp1, exp2, exp3, exp4, exp7, exp5, exp6, exp9, exp10, exp8, exp11]

        # animation of the messages
        SCREEN.fill((0, 0, 0))
        n = 10  # needed to increment y value
        for index in range(4):
            SCREEN.blit(show[index], (5, index * 11 + n))
            n *= 1.25
        pygame.display.flip()

        n = 40  # needed to increment y value
        for index in range(4, 11):
            SCREEN.blit(show[index], (5, index * 12 + n))
            n *= 1.25
        pygame.display.flip()

        # get keyboard input to start or leave the game
        keep = 1
        while keep:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                    
                if event.type == KEYDOWN:
                    if event.key == K_F1:
                        keep = 0

                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()

    @staticmethod
    def winned():
        """Display the success screen. """

        # message to display
        lm = b.BoardSetup.text("Yess ! I'm free !", 28, (242, 202, 0))
        lm2 = b.BoardSetup.text("So long Murdoc !", 28, (242, 202, 0))

        b.BoardSetup.borders()  # refresh the borders to erase the score text
        SCREEN.blit(BG, (10, 10))
        SCREEN.blit(WIN, (25, 40))
        SCREEN.blit(lm, (20, 10))
        SCREEN.blit(lm2, (30, 280))

        pygame.display.flip()
        pygame.time.wait(12000)

    @staticmethod
    def failed():
        """Display the game over screen. """
        fail = pygame.image.load("./ressource/fail_Murdoc.jpg")

        # message to display
        lm = b.BoardSetup.text("I finally got you", 28, (117, 22, 11))
        lm2 = b.BoardSetup.text("MacGyver !!", 28, (117, 22, 11))

        b.BoardSetup.borders()  # refresh the borders to erase the score text
        SCREEN.blit(BG, (10, 10))
        SCREEN.blit(fail, (25, 55))
        SCREEN.blit(lm, (10, 10))
        SCREEN.blit(lm2, (70, 250))

        pygame.display.flip()
        pygame.time.wait(3000)
