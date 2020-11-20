import pygame

import constants
import platforms
from enemy import Enemy

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shiftY = 0
    world_shiftX = 0
    
    level_limit = -1000
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.enemy_sprite = pygame.sprite.Group()
        self.newStart = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.enemy_sprite.update()
        self.newStart.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shiftX // 3, self.world_shiftY // 3))
        screen.blit(constants.map_img, (self.world_shiftX, self.world_shiftY))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.enemy_sprite.draw(screen)
        self.newStart.draw(screen)
    
    def shift_worldY(self, shift_y):
        """ When the user mouse up or down and we need to scroll everything: """
        self.world_shiftY += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y
        
        for enemies in self.enemy_sprite:
            enemies.rect.y += shift_y
        
        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

    def shift_worldX(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shiftX += shift_x


        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemies in self.enemy_sprite:
            enemies.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player, surf):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        

        ground = []
        restart = []
        enemies = []
        for tile_object in constants.myMap.tmxdata.objects:
            if tile_object.name == 'player':
                self.player.rect.x = tile_object.x
                self.player.rect.y = tile_object.y
            if tile_object.name == 'ground':
                ground.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y, tile_object.width])
            if tile_object.name == 'water':
                pygame.draw.rect(surf, constants.RED, (tile_object.x, tile_object.y - 400, tile_object.width, tile_object.height))
            if tile_object.name == 'restart':
                restart.append([platforms.GRASS_DIRT, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'enemy':
                enemies.append(Enemy(tile_object.x, tile_object.y))
    
        for active in enemies:
            self.enemy_sprite.add(active)

        # Go through the array above and add platforms
        for platform in ground:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            block.player = self.player
            self.platform_list.add(block)
