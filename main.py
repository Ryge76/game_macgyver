# _*_ coding: utf-8 _*_

from modules.board import *  # contains defining elements of the board game
from modules.ambiance import *  # contains sound effects
from modules.player import *  # contains main character and phases
from modules.constants import *  # contains constants of the game

pygame.init()

# lists of rectangles for the obstacles, objects to collect, the final door exit and Murdoc the guardian
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

    # initial copy of the screen. Will contain later on a copy of the full board with obstacles etc. to refresh the \
    # background.
    screenshot = SCREEN.copy()

    mac_rect = Player.player()
    Ambiance.ear()

    pygame.key.set_repeat(10, 30)  # set the repeat function for the keyboard
    keep = 1
    while keep:
        # Picking up the objects
        if mac_rect.collidelist(collection) != -1:
            Ambiance.ear("ring")
            collected = BoardSetup.score(1)
            index = mac_rect.collidelist(collection)  # get the index of the colliding object in the collection list
            SCREEN.blit(MASK, mac_rect)  # remove Mac picture from the board before the screenshot
            SCREEN.blit(MASK, collection[index])  # hide the object
            del collection[index]  # remove the object collected from the collection list
            pygame.display.flip()
            screenshot = SCREEN.copy()  # update the background with a scene without the object
            SCREEN.blit(MAC, mac_rect)
            pygame.display.flip()

        # Gard and exit scenario
        if mac_rect.collidelist(garded) != -1:
            if collected < 3:
                # sound effects
                pygame.mixer.music.pause()
                Ambiance.ear("shout")
                # replace Mac pic with a skeleton
                SCREEN.blit(MASK, mac_rect)
                SCREEN.blit(DEATH, mac_rect)
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
            if event.type == QUIT:
                keep = 0

            if event.type == KEYDOWN:  # keyboard'controls of Mac, sound animation, and exit of the program
                if event.key == K_RETURN:
                    pygame.mixer.music.pause()
                if event.key == K_SPACE:
                    pygame.mixer.music.unpause()
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

                if event.key == K_UP and mac_rect.move(0, -3).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(0, -3)
                    SCREEN.blit(screenshot, (0, 0))
                    SCREEN.blit(MAC, mac_rect)
                    pygame.display.flip()

                if event.key == K_DOWN and mac_rect.move(0, 3).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(0, 3)
                    SCREEN.blit(screenshot, (0, 0))
                    SCREEN.blit(MAC, mac_rect)
                    pygame.display.flip()

                if event.key == K_LEFT and mac_rect.move(-3, 0).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(-3, 0)
                    SCREEN.blit(screenshot, (0, 0))
                    SCREEN.blit(MAC, mac_rect)
                    pygame.display.flip()

                if event.key == K_RIGHT and mac_rect.move(3, 0).collidelist(obstacles) == -1:
                    mac_rect = mac_rect.move(3, 0)
                    SCREEN.blit(screenshot, (0, 0))
                    SCREEN.blit(MAC, mac_rect)
                    pygame.display.flip()


if __name__ == "__main__":
    intro()
