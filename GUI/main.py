from settings import *
from buttons import Button
import pygame, sys


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# defined images goes here
playButton = pygame.image.load(path.join(img_dir, "btn1.png")).convert()
quitButton = pygame.image.load(path.join(img_dir, "btn1.png")).convert()
nextButton = pygame.image.load(path.join(img_dir, "btn2.png")).convert()

bg1 = pygame.image.load(path.join(img_dir, "bg1.png")).convert()
bg2 = pygame.image.load(path.join(img_dir, "bg2.png")).convert()
aofbg = pygame.image.load(path.join(img_dir, "aof.png")).convert()

all_sprites = pygame.sprite.Group()
buttons = pygame.sprite.Group()

# Buttons are listed here eacch button does something different
# They have different indexes
btn1 = Button(playButton, 120, 50, 0,10, "Play", "vertical")
btn2 = Button(quitButton, 120, 50, 0,20, "Quit", "vertical")
btn3 = Button(nextButton, 120, 50, 0,60, "Next", "vertical")


clock = pygame.time.Clock()
index = 1
color = WHITE

blitX = 0
buttonGroup = []
buttonName = ['Play', 'Next']

for btn in range(2):
    buttonGroup.append(Button(playButton, 120, 50, 0,10 * btn, buttonName[btn], "vertical"))
    all_sprites.add(buttonGroup[btn])
    buttons.add(buttonGroup[btn])
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or index == 5:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for listener in buttons:
                value = listener.onClick(event, index)
                index = value
                listener.kill()

    if index == 1:
        color = GREEN
        for mx in buttonGroup:
            all_sprites.add(mx)
            buttons.add(mx)
        screen.fill(color)
        
    elif index == 2:
        color = WHITE
        screen.fill(color)
        all_sprites.add(btn2)
        buttons.add(btn2)
        x = blitX % bg1.get_rect().width

        blitX -= 2
        screen.blit(bg1, (x - bg1.get_rect().width, 0))
        if x < 600:
            screen.blit(bg2, (x , 0))

    elif index == 3:
        color = GREEN
        screen.fill(color)
        all_sprites.add(btn1)
        buttons.add(btn1)
        screen.blit(aofbg, (0,0))
    else:
        color = RED

    all_sprites.draw(screen)
    pygame.display.update()
        

        

