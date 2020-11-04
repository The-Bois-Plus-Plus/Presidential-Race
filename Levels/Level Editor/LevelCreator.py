import pygame
from os import path

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Video Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH  = 600
HEIGHT = 600 
class Map:
    def __init__(self, fileName):
        self.data = []
        with open(fileName, 'rt') as f:
                  for line in f:
                      self.data.append(line)
                  
        self.tileWidth  = len(self.data[0])
        self.tileHeight = len(self.data)
        self.width      =  self.tileWidth * 20
        self.height     = self.tileHeight * 20

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width  = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        # where is the camera targeting?
        # It is targeting the player
        x = -target.rect.x + int(WIDTH  / 2)
        y = -target.rect.y + int(HEIGHT / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        
    def update(self):
        self.rect.x = self.x * 20
        self.rect.y = self.y * 20
        
game_folder = path.dirname(__file__)
myMap = Map(path.join(game_folder, 'level1.txt'))

all_sprites = pygame.sprite.Group()
player = Player(10, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # draw 
        for x in range(0, 600, 20):
            pygame.draw.line(screen, LIGHTGREY, (x, 0), (x, 600))
            for y in range(0, 600, 20):
                pygame.draw.line(screen, LIGHTGREY, (0, y), (600, y))

        camera = Camera(myMap.width, myMap.height)

      
        # enumerate each time it runs throught the list you will get the index and the value
        y = 0
        for row, tiles in enumerate(myMap.data):
            x = 0
            y += 1
            for col, tile in enumerate(tiles):
                x+= 1
                if tile == '1':
                    pygame.draw.rect(screen, GREEN, (x * 20, y * 20, 20, 20))
                if tile == '2':
                    pygame.draw.rect(screen, RED, (x * 20, y * 20, 20, 20))
        
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))
        camera.update(player)
        pygame.display.update()
