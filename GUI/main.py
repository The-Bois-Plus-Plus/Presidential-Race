from settings import *
from buttons import Button
import pygame, sys


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))





# scroller test with panel and scroller
itemNavigate = []
itemloc = [] # the location of the items if i ever want to manually set the location
items = []   #the actual items in the list

for it in range(3):
    items.append(it)
    itemNavigate.append(items[it])


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
btn2 = Button(quitButton, 120, 50, 0,20, "Next", "vertical")
btn3 = Button(nextButton, 120, 50, 0,60, "Quit", "vertical")


clock = pygame.time.Clock()
index = 1
color = WHITE

blitX = 0
buttonGroup = []
# menu for program.
buttonName = ['Quit', 'Next']

scrollY = 150
for btn in range(2):
    buttonGroup.append(Button(playButton, 120, 50, 0,10 * btn, buttonName[btn], "vertical"))
    all_sprites.add(buttonGroup[btn])
    buttons.add(buttonGroup[btn])
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or index == 7:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for listener in buttons:
                value = listener.onClick(event, index)
                index = value
                listener.kill()
        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_DOWN:
        #        if scrollY > 120:
         #           scrollY -= 2
          #  if event.key == pygame.K_UP:
           #     if scrollY < 170:
            #        scrollY += 2


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
        pygame.draw.rect(screen, GREY, (x - 90, 390, 90, 90))
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

    #pygame.draw.rect(screen, RED,(150, 120, 300, 400))

    #scroll bar goes here
    #pygame.draw.rect(screen, WHITE, (450, 120, 10, 400))

   # for item in items:
        #scroll widget
   #     pygame.draw.rect(screen,  GREY, (450, scrollY * -1 + 300, 10,100 + 90 * item * 1.3))
   #     pygame.draw.rect(screen, WHITE, (200, scrollY + 90 * item * 1.3, 200, 100))
        
    all_sprites.draw(screen)
    pygame.display.update()
        

        

