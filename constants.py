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


myMap1 = TileMap('level1.tmx')
myMap2 = TileMap('level2.tmx')
myMap3 = TileMap('level3.tmx')
map_img1 = myMap1.make_map()
map_img2 = myMap2.make_map()
map_img3 = myMap3.make_map()
map_img1.set_colorkey(BLACK)
map_img2.set_colorkey(BLACK)
map_img3.set_colorkey(BLACK)
map_rect = map_img1.get_rect()

pygame.quit()