"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

import platforms
from platforms import MovingPlatform
from spritesheet import SpriteSheet


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # constructor for player level
    level = None

    # -- Methods
    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("graphicsLib/Player/trump_run.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(39, 0, 58, 80)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(150, 0, 58, 80)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(261, 0, 58, 80)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(372, 0, 58, 80)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(484, 0, 59, 80)
        self.walking_frames_r.append(image)
        # image = sprite_sheet.get_image(569, 0, 55, 80)
        # self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 256, 256, 256)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(256, 256, 256, 256)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(512, 256, 256, 256)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(768, 256, 256, 256)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(1024, 256, 256, 256)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(1280, 256, 256, 256)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.touchingGround = True
        self.health = 100
        self.life = 3

    def update(self):
        """ Move the player. """
        # Gravity
        self.touchingGround = True
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shiftX
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        self.mask = pygame.mask.from_surface(self.image)
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        # self.touchingGround = True
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y


        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            # elif self.change_y < 0:
            #     self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
    def calc_grav(self):
        """ Calculate effect of gravity. """
        # self.touchingGround = False

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            self.touchingGround = False
            #print(self.change_y)


        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
        

    def jump(self):
        """ Called when user hits 'jump' button. """
        self.touchingGround = True
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -11

    def bounce(self, _bounce):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -_bounce
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 4
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
