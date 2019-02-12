# _*_ coding: utf-8 _*_
import pygame

import pygame.locals as pl
import modules.board as mb
import modules.constants as mc


class Player():
    """Functions related to the player: picture,
    animation, success/failure screen, game's rules. """
    @staticmethod
    def player():
        """Create MacGyver player on the board
        and rectangle to animate him. """

        mac_rect = mc.MAC.get_rect()
        mac_rect = mac_rect.move(20, 20)
        mc.SCREEN.blit(mc.MAC, mac_rect)
        pygame.display.flip()
        return mac_rect

    @staticmethod
    def intro():
        """Display initial splash screen. """

        mc.SCREEN.fill((0, 0, 0))
        mc.SCREEN.blit(mc.INTRO, (0, 45))
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

        exp1 = mb.BoardSetup.text("Help MacGyver escape the labyrinth.", 15)
        exp2 = mb.BoardSetup.text("Alive... ;-)", 15, (255, 0, 0))
        exp3 = mb.BoardSetup.text("For that you will need 3 objects.", 15)
        exp4 = mb.BoardSetup.text("Find them and get rid of Murdoc !", 15)
        exp5 = mb.BoardSetup.text("Use ARROW KEYS to move.",
                                  15, (255, 255, 0))
        exp6 = mb.BoardSetup.text("Press ENTER to stop the music.",
                                  15, (255, 255, 0))
        exp9 = mb.BoardSetup.text("Press SPACE to resume the music.",
                                  15, (255, 255, 0))
        exp7 = mb.BoardSetup.text("During the game: ",
                                  15, (255, 255, 0))
        exp8 = mb.BoardSetup.text("Ready ? ==> Press F1 to start !",
                                  15, (0, 255, 0))
        exp11 = mb.BoardSetup.text("Afraid ? ==> Press ESCAPE to quit...",
                                   15, (255, 0, 0))
        exp10 = mb.BoardSetup.text("Press ESCAPE to exit game.",
                                   15, (255, 255, 0))

        # list of message to display
        show = [exp1, exp2, exp3, exp4, exp7, exp5,
                exp6, exp9, exp10, exp8, exp11]

        # animation of the messages
        mc.SCREEN.fill((0, 0, 0))
        n = 10  # needed to increment y value
        for index in range(4):
            mc.SCREEN.blit(show[index], (5, index * 11 + n))
            n *= 1.25
        pygame.display.flip()

        n = 40  # needed to increment y value
        for index in range(4, 11):
            mc.SCREEN.blit(show[index], (5, index * 12 + n))
            n *= 1.25
        pygame.display.flip()

        # get keyboard input to start or leave the game
        keep = True
        while keep:
            for event in pygame.event.get():
                if event.type == pl.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pl.KEYDOWN:
                    if event.key == pl.K_F1:
                        keep = False

                    if event.key == pl.K_ESCAPE:
                        pygame.quit()
                        quit()

    @staticmethod
    def winned():
        """Display the success screen. """

        # message to display
        lm = mb.BoardSetup.text("Yess ! I'm free !", 28, (242, 202, 0))
        lm2 = mb.BoardSetup.text("So long Murdoc !", 28, (242, 202, 0))

        mb.BoardSetup.borders()  # refresh the borders to erase the score text
        mc.SCREEN.blit(mc.BG, (10, 10))
        mc.SCREEN.blit(mc.WIN, (25, 40))
        mc.SCREEN.blit(lm, (20, 10))
        mc.SCREEN.blit(lm2, (30, 280))

        pygame.display.flip()
        pygame.time.wait(12000)

    @staticmethod
    def failed():
        """Display the game over screen. """
        fail = pygame.image.load("./ressource/fail_Murdoc.jpg")

        # message to display
        lm = mb.BoardSetup.text("I finally got you", 28, (117, 22, 11))
        lm2 = mb.BoardSetup.text("MacGyver !!", 28, (117, 22, 11))

        mb.BoardSetup.borders()  # refresh the borders to erase the score text
        mc.SCREEN.blit(mc.BG, (10, 10))
        mc.SCREEN.blit(fail, (25, 55))
        mc.SCREEN.blit(lm, (10, 10))
        mc.SCREEN.blit(lm2, (70, 250))

        pygame.display.flip()
        pygame.time.wait(3000)
