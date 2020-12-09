import pygame

import constants
import platforms
import random
from player import Player
from enemy import Enemy
from voter_mail import PowerUp

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
    def __init__(self):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.lava_platform = pygame.sprite.Group()
        self.enemy_list    = pygame.sprite.Group()
        self.enemy_mov     = pygame.sprite.Group()
        self.enemy_sprite  = pygame.sprite.Group()
        self.new_level     = pygame.sprite.Group()
        self.player        = None
        self.vote_list     = pygame.sprite.Group()
        # self.respawn_list = pygame.sprite.Group()
        self.level_change = 0

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.lava_platform.update()
        self.enemy_list.update()
        self.enemy_mov.update()
        self.new_level.update()
        self.enemy_sprite.update()
        self.vote_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shiftX // 3, self.world_shiftY // 3))
        mipMap = [constants.map_img1, constants.map_img2, constants.map_img3]
        screen.blit(mipMap[self.level_change], (self.world_shiftX, self.world_shiftY - 400))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.enemy_mov.draw(screen)
        self.enemy_sprite.draw(screen)
        self.vote_list.draw(screen)
        self.new_level.draw(screen)
        self.lava_platform.draw(screen)
        # self.respawn_list.draw(screen)
    
    def shift_worldY(self, shift_y):
        """ When the user mouse up or down and we need to scroll everything: """
        self.world_shiftY += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y
        
        for enemies in self.enemy_sprite:
            enemies.rect.y += shift_y
        
        for mov in self.enemy_mov:
            mov.rect.y += shift_y
        
        for platform in self.lava_platform:
            platform.rect.y += shift_y

        for mail in self.vote_list:
            mail.rect.y += shift_y
        
        for new in self.new_level:
            new.rect.y += shift_y
        
        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

    def shift_worldX(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shiftX += shift_x


        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
        
        for platform in self.lava_platform:
            platform.rect.x += shift_x 

        for enemies in self.enemy_sprite:
            enemies.rect.x += shift_x
        
        for mov in self.enemy_mov:
            mov.rect.x += shift_x
        
        for mail in self.vote_list:
            mail.rect.x += shift_x
        
        for new in self.new_level:
            new.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self)

        self.background = pygame.image.load("images/background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        
        ground  = []
        enemies = []
        movenemy = []
        self.power   = []
        self.resetX = 0
        self.resetY = 0
        lava    = []
        finish  = []
        for tile_object in constants.myMap1.tmxdata.objects:
            if tile_object.name == 'ground':
                ground.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'enemy':
                enemies.append([Enemy(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'move':
                movenemy.append([Enemy(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'mail':
                self.power.append([PowerUp(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'lava':
                lava.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'finish':
                finish.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'player':
                self.player = Player(tile_object.x, tile_object.y - 400)
                self.resetX = tile_object.x
                self.resetY = tile_object.y - 400
                


        for active in enemies:
            self.enemy_sprite.add(active)

        for mov in movenemy:
            self.enemy_mov.add(mov)

        for votes in self.power:
            self.vote_list.add(votes)


        # Go through the array above and add platforms
        for platform in ground:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.platform_list.add(block)

        # we want to add the lava
        for platform in lava:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.lava_platform.add(block)
        
        for platform in finish:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.new_level.add(block)

    def restart(self):
        del self.power[:]
        for votes in self.vote_list:
            votes.kill()

        for tile_object in constants.myMap1.tmxdata.objects:
            if tile_object.name == 'mail':
                self.power.append([PowerUp(tile_object.x, tile_object.y - 400)])

        for votes in self.power:
            self.vote_list.add(votes)

    def resetMov(self):
        if (self.resetX and self.resetY != None):
            self.player.rect.x = self.resetX
            self.player.rect.y = self.resetY

class Level_02(Level):
    def __init__(self):
        # Call the parent constructor
        Level.__init__(self)

        self.background = pygame.image.load("images/background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        
        ground  = []
        enemies = []
        movenemy = []
        self.power   = []
        self.resetX = 0
        self.resetY = 0
        lava    = []
        finish  = []
        for tile_object in constants.myMap2.tmxdata.objects:
            if tile_object.name == 'ground':
                ground.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'enemy':
                enemies.append([Enemy(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'move':
                movenemy.append([Enemy(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'mail':
                self.power.append([PowerUp(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'lava':
                lava.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'finish':
                finish.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'player':
                self.player = Player(tile_object.x, tile_object.y - 400)
                self.resetX = tile_object.x
                self.resetY = tile_object.y - 400
                


        for active in enemies:
            self.enemy_sprite.add(active)

        for mov in movenemy:
            self.enemy_mov.add(mov)

        for votes in self.power:
            self.vote_list.add(votes)


        # Go through the array above and add platforms
        for platform in ground:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.platform_list.add(block)

        # we want to add the lava
        for platform in lava:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.lava_platform.add(block)
        
        for platform in finish:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.new_level.add(block)

    def restart(self):
        del self.power[:]
        for votes in self.vote_list:
            votes.kill()

        for tile_object in constants.myMap2.tmxdata.objects:
            if tile_object.name == 'mail':
                self.power.append([PowerUp(tile_object.x, tile_object.y - 400)])

        for votes in self.power:
            self.vote_list.add(votes)

    def resetMov(self):
        if (self.resetX and self.resetY != None):
            self.player.rect.x = self.resetX
            self.player.rect.y = self.resetY

class Level_03(Level):
    def __init__(self):
        # Call the parent constructor
        Level.__init__(self)

        self.background = pygame.image.load("images/background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        
        ground  = []
        enemies = []
        movenemy = []
        self.power   = []
        self.resetX = 0
        self.resetY = 0
        lava    = []
        finish  = []
        for tile_object in constants.myMap3.tmxdata.objects:
            if tile_object.name == 'ground':
                ground.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'enemy':
                enemies.append([Enemy(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'move':
                movenemy.append([Enemy(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'mail':
                self.power.append([PowerUp(tile_object.x, tile_object.y - 400)])
            if tile_object.name == 'lava':
                lava.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'finish':
                finish.append([platforms.EMPTY_PLATFORM, tile_object.x, tile_object.y - 400, tile_object.width])
            if tile_object.name == 'player':
                self.player = Player(tile_object.x, tile_object.y - 400)
                self.resetX = tile_object.x
                self.resetY = tile_object.y - 400
                


        for active in enemies:
            self.enemy_sprite.add(active)

        for mov in movenemy:
            self.enemy_mov.add(mov)

        for votes in self.power:
            self.vote_list.add(votes)


        # Go through the array above and add platforms
        for platform in ground:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.platform_list.add(block)

        # we want to add the lava
        for platform in lava:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.lava_platform.add(block)
        
        for platform in finish:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.rect.w = platform[3]
            # block.player = self.player
            self.new_level.add(block)

    def restart(self):
        del self.power[:]
        for votes in self.vote_list:
            votes.kill()

        for tile_object in constants.myMap3.tmxdata.objects:
            if tile_object.name == 'mail':
                self.power.append([PowerUp(tile_object.x, tile_object.y - 400)])

        for votes in self.power:
            self.vote_list.add(votes)

    def resetMov(self):
        if (self.resetX and self.resetY != None):
            self.player.rect.x = self.resetX
            self.player.rect.y = self.resetY


