# _*_ coding: utf-8 _*_
import pygame
import pygame.locals as pl

from modules.board import BoardSetup
from modules.ambiance import Ambiance  # contains sound effects
from modules.player import Player  # contains main character and phases
import modules.constants as mc

pygame.init()

# lists of rectangles for the obstacles, objects to collect, \
# the final door exit and Murdoc the guardian
obstacles = list()
collection = list()
garded = list()
# number of collected objects
collected = 0


def intro():
    """Display the introduction screens of the game. """
    Player.intro()
    start()


def start():
    """Initializing the game board and the player controls. """
    global obstacles, collection, garded, collected
    # setting the lists and variable (necessary to restart the game properly)
    garded[:], collection[:], obstacles[:] = [], [], []
    collected = 0

    garded = BoardSetup.board()
    BoardSetup.walls()
    obstacles = BoardSetup.borders()
    collection = BoardSetup.objects()
    BoardSetup.score()

    # initial copy of the screen. Will contain later on \
    # a copy of the full board with obstacles etc \
    # to refresh the background.
    screenshot = mc.SCREEN.copy()

    mac_rect = Player.player()
    Ambiance.ear()

    pygame.key.set_repeat(10, 30)  # set the repeat function for the keyboard
    keep = True
    while keep:
        # Picking up the objects
        if mac_rect.collidelist(collection) != -1:
            Ambiance.ear("ring")
            collected = BoardSetup.score(1)
            # get the index of the colliding object in the collection list
            index = mac_rect.collidelist(collection)
            # remove Mac picture from the board before the screenshot
            mc.SCREEN.blit(mc.MASK, mac_rect)
            mc.SCREEN.blit(mc.MASK, collection[index])  # hide the object
            # remove the object collected from the collection list
            del collection[index]
            pygame.display.flip()
            # update the background with a scene without the object
            screenshot = mc.SCREEN.copy()
            mc.SCREEN.blit(mc.MAC, mac_rect)
            pygame.display.flip()

        # Gard and exit scenario
        if mac_rect.collidelist(garded) != -1:
            if collected < 3:
                # sound effects
                pygame.mixer.music.pause()
                Ambiance.ear("shout")
                # replace Mac pic with a skeleton
                mc.SCREEN.blit(mc.MASK, mac_rect)
                mc.SCREEN.blit(mc.DEATH, mac_rect)
                pygame.display.flip()

                pygame.time.wait(2000)
                Player.failed()

                start()

            else:
                Ambiance.ear("clap")
                pygame.mixer.music.fadeout(500)

                Player.winned()
            # resetting the lists and variable
                garded[:], collection[:], obstacles[:] = [], [], []
                collected = 0

                start()

        for event in pygame.event.get():
            if event.type == pl.QUIT:
                keep = False
            # keyboard'controls of Mac, sound, and exit of the program
            if event.type == pl.KEYDOWN:
                if event.key == pl.K_RETURN:
                    pygame.mixer.music.pause()
                if event.key == pl.K_SPACE:
                    pygame.mixer.music.unpause()
                if event.key == pl.K_ESCAPE:
                    pygame.quit()
                    exit()

                if event.key == pl.K_UP \
                        and mac_rect.move(0, -3).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(0, -3)
                    mc.SCREEN.blit(screenshot, (0, 0))
                    mc.SCREEN.blit(mc.MAC, mac_rect)
                    pygame.display.flip()

                if event.key == pl.K_DOWN \
                        and mac_rect.move(0, 3).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(0, 3)
                    mc.SCREEN.blit(screenshot, (0, 0))
                    mc.SCREEN.blit(mc.MAC, mac_rect)
                    pygame.display.flip()

                if event.key == pl.K_LEFT \
                        and mac_rect.move(-3, 0).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(-3, 0)
                    mc.SCREEN.blit(screenshot, (0, 0))
                    mc.SCREEN.blit(mc.MAC, mac_rect)
                    pygame.display.flip()

                if event.key == pl.K_RIGHT \
                        and mac_rect.move(3, 0).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(3, 0)
                    mc.SCREEN.blit(screenshot, (0, 0))
                    mc.SCREEN.blit(mc.MAC, mac_rect)
                    pygame.display.flip()


if __name__ == "__main__":
    intro()
