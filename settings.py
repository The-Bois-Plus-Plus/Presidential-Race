from os import path
import pygame

"""
    The settings is a list of predfined values.
"""

# this is the width of the screen
WIDTH  = 600
HEIGHT = 600


RED   = (255,     0,    0)
GREEN = (0  ,   255,    0)
WHITE = (255,   255,  255)
BLACK = (  0,     0,    0)
GREY  = ( 45,    45,   45)

pygame.mixer.init()
#snd_dir = path.join(path.dirname(__file__), 'snd')
#btn_snd = pygame.mixer.Sound(path.join(snd_dir, 'Hit_Hurt1.wav'))

# The directory we are pulling these images out of.
#img_dir = path.join(path.dirname(__file__), 'img')
