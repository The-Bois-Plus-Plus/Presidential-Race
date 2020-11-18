import pygame
from settings import *
from constants import BLUE
from PIL import Image, ImageEnhance

class Button(pygame.sprite.Sprite):
    def __init__(self, image, width, height, x, y, text ='', stack=None):
        pygame.sprite.Sprite.__init__(self)
        self.stack = stack
        self.width  = width
        self.height = height
        self.image = image
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.highlight = False
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2

        if self.stack == 'vertical':
            self.rect.x = self.rect.centerx - (self.width  / 2) + 103
            self.rect.y = 160 + y * 3.6
        else:
            self.rect.x = x
            self.rect.y = y
        self.text   = text
        if (self.text != '' and self.text != "Back/Arrow"):
            self.font = pygame.font.Font(None, 20)
            self.surf = self.font.render(self.text, True, BLACK)
            imgW = self.surf.get_width()
            imgH = self.surf.get_height()
            self.image.blit(self.surf, [width/2 - imgW/2, height/2 - imgH/2])
    def animation(self):
        light = pygame.Surface((self.image.get_width(), self.image.get_height()),flags=pygame.SRCALPHA)
        light.fill(self.highlight)
        self.image.blit(light, (0, 0), special_flags=pygame.BLEND_RGBA_MAX)
    def hover(self, event):
        if self.rect.collidepoint(event.pos):
            self.animation()
            self.highlight = True
        else:
            self.highlight = False

    def onClick(self, event, index):
        if self.rect.collidepoint(event.pos):
            #btn_snd.play()
            if self.text == 'Play':
                index = 7
            elif self.text == 'Store':
                index = 10
            elif self.text == 'Quit':
                index = 8
            elif self.text == 'Settings':
                index = 3
            elif self.text == 'Help':
                index = 4
            elif self.text == 'Back/Arrow' or self.text == 'Back':
                if index >= 3 and index != 5:
                    index = 1
                else:
                    index -= 1
            elif self.text == 'Next':
                if index > 4:
                    pass
                else:
                    index += 1
            elif self.text == 'Yes':
                index = 5
            elif self.text == 'No':
                index = 6
            elif self.text == 'Save':
                # we want to save the image
                pass
            else:
                index = 0
        return index

class Panel(pygame.sprite.Sprite):
    def __init__(self, image, width, height, x, y, text=''):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = image
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        if (self.text != ''):
            self.font = pygame.font.Font(None, 20)
            self.surf = self.font.render(self.text, True, (255, 0, 0))
            imgW = self.surf.get_width()
            imgH = self.surf.get_height()
            self.image.blit(self.surf, [imgW/2, height/2 + imgH/2 + 20])
    def onClick(self, event, index):
        if self.rect.collidepoint(event.pos):
            if self.text == 'Level1':
                index = 6
            elif self.text == 'Level2':
                index = 8
            elif self.text == 'Level3':
                index = 9
            else:
                index = 0
        return index
