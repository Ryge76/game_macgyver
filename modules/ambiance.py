# _*_ coding:utf-8 _*_
import pygame


class Ambiance():
    """Game sound effects. """
    @staticmethod
    def ear(sound=""):
        """ Create musical ambiance of the game. """

        fx = sound
        pl = dict()

        # sound effects
        ring = pygame.mixer.Sound("./ressource/sonnette_velo.ogg")
        shout = pygame.mixer.Sound("./ressource/cri.ogg")
        clap = pygame.mixer.Sound("./ressource/bravo.ogg")

        pl.update({"ring": ring, "shout": shout, "clap": clap})

        if fx in pl.keys():
            pl[fx].play()
        else:
            pygame.mixer.music.load("./ressource/ambiance_def.ogg")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(5)
