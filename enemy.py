"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

import platforms
from platforms import MovingPlatform
from spritesheet import SpriteSheet


class Enemy(pygame.sprite.Sprite):
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

        sprite_sheet = SpriteSheet("graphicsLib/Enemies/china_virus.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 50, 50)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 0, 50, 50)
        self.walking_frames_r.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]


        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y  
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("images/slimeWalk1.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 49, 28)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 0, 59, 12)
        self.walking_frames_r.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]


        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        # Move up/down
        self.rect.y += self.change_y


        # Check and see if we hit anything
   
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
            #print(self.change_y)


        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
        

    def jump(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.change_y = -10
        # If it is ok to jump, set our speed upwards
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
       