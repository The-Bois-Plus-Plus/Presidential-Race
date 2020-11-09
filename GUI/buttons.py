import pygame
from settings import *


class Button(pygame.sprite.Sprite):
    def __init__(self, image, width, height, x, y, text ='', stack = None):
        pygame.sprite.Sprite.__init__(self)
        self.stack = stack
        self.width  = width
        self.height = height
        self.image = image
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        if self.stack == '':
            self.rect.x = x
            self.rect.y = y
        elif self.stack == 'vertical':
            self.rect.x = self.rect.centerx - (self.width  / 2)
            self.rect.y = y * 4
        elif self.stack == 'horizontal':
            self.rect.x = self.rect.x * 2
            self.rect.y = x
        self.text   = text
        if (self.text != ''):
            self.font = pygame.font.Font(None, 20)
            self.surf = self.font.render(self.text, True, BLACK)
            imgW = self.surf.get_width()
            imgH = self.surf.get_height()
            self.image.blit(self.surf, [width/2 - imgW/2, height/2 - imgH/2])
            
    def onClick(self, event, index):
        if self.rect.collidepoint(event.pos):
            btn_snd.play()
            if self.text == 'Play':
                index = 1
            elif self.text == 'Quit':
                index = 3
            elif self.text == 'Next':
                if index > 4:
                    pass
                else:
                    index += 1
            elif self.text == 'Yes':
                index = 5
            elif self.text == 'No':
                index = 6
            else:
                index = 0
        return index


# Panel Class Goes down here. This class will be responsible for holding other objects.
class Panel(pygame.sprite.Sprite):
    all_sprites = pygame.sprite.Group()
    def __init__(self):
        pass
