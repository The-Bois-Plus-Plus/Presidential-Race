import pygame, random

#from platforms import MovingPlatform
from spritesheet import SpriteSheet
import constants

class PowerUp(pygame.sprite.Sprite):

    level = None
    change_x = 0
    change_y = 0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
       
        sprite_sheet = SpriteSheet("images/voter_mail.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 28, 20)
        self.image = image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
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

 
        # # Check and see if we hit anything

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            # if isinstance(block, MovingPlatform):
            #     self.rect.x += block.change_x