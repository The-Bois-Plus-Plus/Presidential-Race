"""
Global constants
"""
import pygame
from tilemap import TileMap
# Colors
BLACK    = (   0,   0,   0) 
BLUE     = (   0,   0, 255)
WHITE    = ( 255, 255, 255) 
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)

pygame.init()
pygame.display.set_mode((10,10))
# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600


myMap = TileMap('level1.tmx')
map_img = myMap.make_map()
map_img.set_colorkey(BLACK)
map_rect = map_img.get_rect()

pygame.quit()