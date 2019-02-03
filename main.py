# _*_ coding: utf-8 _*_

from modules.board import *  # contains defining elements of the board game
from modules.ambiance import *  # contains sound effects
from modules.player import *  # contains


pygame.init()

# Setting display
screen = pygame.display.set_mode((320, 320))
pygame.display.set_caption("Mac-mare: help me out !")

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
    screenshot = screen.copy()

    mac, mac_rect = Player.player()
    Ambiance.ear()

    mask = pygame.image.load("./ressource/floor_mask2.png").convert()  # image to mask the collected objects
    death = pygame.image.load("./ressource/mort.png")  # image of failed mission

    pygame.key.set_repeat(10, 30)  # set the repeat function for the keyboard
    keep = 1
    while keep:
        # Picking up the objects
        if mac_rect.collidelist(collection) != -1:
            Ambiance.ear("ring")
            collected = BoardSetup.score(1)
            index = mac_rect.collidelist(collection)  # get the index of the colliding object in the collection list
            screen.blit(mask, mac_rect)  # remove Mac picture from the board before the screenshot
            screen.blit(mask, collection[index])  # hide the object
            del collection[index]  # remove the object collected from the collection list
            pygame.display.flip()
            screenshot = screen.copy()  # update the background with a scene without the object
            screen.blit(mac, mac_rect)
            pygame.display.flip()

        # Gard and exit scenario
        if mac_rect.collidelist(garded) != -1:
            if collected < 3:
                # sound effects
                pygame.mixer.music.pause()
                Ambiance.ear("shout")
                # replace Mac pic with a skeleton
                screen.blit(mask, mac_rect)
                screen.blit(death, mac_rect)
                pygame.display.flip()

                pygame.time.wait(2000)
                Player.failed()

                # # resetting the lists and variable
                # garded[:], collection[:], obstacles[:] = [], [], []
                # collected = 0
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
    intro()
