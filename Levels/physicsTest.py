import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 40


pygame.init()
screen = pygame.display.set_mode((600, 600))

all_sprites = pygame.sprite.Group()
player = Player()

all_sprites.add(player)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    all_sprites.draw(screen)
    
    all_sprites.update()
    pygame.display.update()
