"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller example.

From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame
import pathlib
import levels
from constants import *

from buttons import Button, Panel
from platforms import *
from img import *
from os import path
from tilemap import TileMap

from player import Player
from enemy import Enemy
from voter_mail import PowerUp

pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Team Project")

img_dir = path.join(path.dirname(__file__), 'img')
playButton = pygame.image.load(path.join(img_dir, "btn1.png")).convert()
gameMenu   = pygame.image.load("presidentrunMenu.png")
helpnav1   = pygame.image.load("help.png")
backButton = pygame.image.load(path.join(img_dir,"btn2.png")).convert()
backArrow = pygame.image.load(path.join(img_dir, "arrow.png")).convert()
level1Icon = pygame.image.load("screen.png").convert()
storeLink = pygame.image.load(path.join(img_dir, "storebtnOrange.png")).convert()
heartImg  = pygame.image.load(path.join(img_dir, "hearts.png")).convert()
storeImg  = pygame.image.load("store.png").convert()
vendetta  = pygame.image.load("vendetta.png").convert()
speedBoost = pygame.image.load("speedBoost.png").convert()
health    = pygame.image.load("health.png").convert()
playerImg = pygame.image.load(path.join(img_dir, "p1_walk02.png")).convert()
playerImg.set_colorkey(BLACK)
playerImg = pygame.transform.scale(playerImg, (160,190))
heartImg.set_colorkey(WHITE)


storeImages = [vendetta, speedBoost, health]
# enhancer = ImageEnhance.Brightness(newImg)
# im_output = enhancer.enhance(0.5)
# im_output.save('brighter-img.png')

# We add all the sprites in a group the reason for this is so that we can check for
# collision between different groups of sprites.
btn1 = Button(playButton, 220, 105, 0,10, "Play", "vertical")
btn5 = Button(playButton, 220, 105, 0,10, "Next", "vertical")
btn2 = Button(playButton, 220, 105, 0,30,"Settings", "vertical")
btn4 = Button(playButton, 220, 105, 0,50, "Help", "vertical")
btn3 = Button(backArrow, 60, 90, 0,10, "Back/Arrow")
btn7 = Button(backButton, 220, 120, 0, 30, "Back")
btn6 = Button(playButton, 220, 105, 500,20, "Save")
btn8 = Button(storeLink, 220, 105,SCREEN_WIDTH/2 - 105, SCREEN_HEIGHT - 180, "Store")

active_sprite_list = pygame.sprite.Group()
buttons = pygame.sprite.Group()
panels = pygame.sprite.Group()
walls = pygame.sprite.Group()

player = Player()
level_list = []
level_list.append(levels.Level_01(player, screen))

current_level = level_list[0]

#player.level = current_level
# Create all the levels
#level_list = []
#level_list.append(levels.Level_02(player))
#level_list.append(levels.Level_03(player))

# Set the current level
#current_level = level_list[1]


# create the game selection
levels = []
for x in range(3):
    levels.append(Panel(level1Icon, 200, 150, 100 + x * 210, 100, 'Level{}'.format(x + 1)))

shop = []
for x in range(3):
    shop.append(Panel(storeImages[x], 100, 100, 360 + x * 105, 110,'Item{}'.format(x + 1)))

def draw_healthBar(surf, x, y, pct):
    if pct < 0:
        pct = 0

    length = 100
    height = 15
    outline = pygame.Rect(x, y, length, height)
    pygame.draw.rect(surf, (0, 255, 0), (x, y, pct, height))
    pygame.draw.rect(surf, (255, 255, 255),outline, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 40 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def refresh():
    for actives in active_sprite_list:
        actives.kill()
    for btn in buttons:
        btn.kill()


    
def LevelOverView():
    refresh()
    
def mainMenu():
    refresh()
    #for oldmembers in active_sprite_list:
        #   oldmembers.kill()
    screen.blit(gameMenu, (0,0))
    buttons.add(btn1)
    buttons.add(btn2)
    buttons.add(btn4)
    buttons.add(btn8)
    active_sprite_list.add(btn1)
    active_sprite_list.add(btn2)
    active_sprite_list.add(btn4)
    active_sprite_list.add(btn8)


# When you clicke the play button this should bring you to all the levels
# inside the game.
def levelSelection():
    refresh()
    for lvl in range(3):
         active_sprite_list.add(levels[lvl])
         panels.add(levels[lvl])
        #pygame.draw.rect(screen, (255,0,0), (100 + x * 210, 100, 200, 150))
     # this is the back button. It takes you back
    buttons.add(btn3) 
    btn3.rect.x = 315
    btn3.rect.y = 400
    active_sprite_list.add(btn3)
    
def gameOver():
    refresh()
    
def gameSettings():
    refresh()
    
def gameHelp():
    refresh()
    
def gameStore():
    refresh()
    for shape_shop in range(3):
        active_sprite_list.add(shop[shape_shop])
        panels.add(shop[shape_shop])

#    enhancements = ['jump', 'run', 'life']


#When the game starts the user will be placed 340 pixels away from the left screen.
player.rect.x = 140
# After the player will then be shifted upwards
player.rect.y = SCREEN_HEIGHT - player.rect.height - 140

def level1():
    refresh()
def level2():
    refresh()
    screen.fill((0,0,0))

    player.level = current_level

    current_level.draw(screen)
    # # This draws the player health bar.
    active_sprite_list.add(player)
 
    draw_healthBar(screen, 5, 5, player.health)
    draw_lives(screen, SCREEN_WIDTH - 140, 5, player.life, heartImg)
def level3():
    refresh()

def main():
    """ Main Program """
    global screen
    pause = False


    # Create the player
    #player = Player()
    #mob = Enemy()

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    index = 1
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEMOTION:
                if index == 1 or index == 3 or index == 4 or index == 5 or index == 7: #or index == 8:
                    for listener in buttons:
                        listener.hover(event)
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if index <= 10: #or index == 8:
                    for listener in buttons:
                        value = listener.onClick(event, index)
                        index = value
                        if (index == 8):
                            pygame.image.save(screen, "screen.png")
                if index == 7:
                    for panel in panels:
                        value = panel.onClick(event, index)
                        index = value
        if index == 6:
            level1()
            # The mob group. The player can interact with the mob group.
            mob_list = pygame.sprite.Group()
            # The power up group. The player interacts with the powerups because they are in a group.
            powerUp_list = pygame.sprite.Group()

            # When the game starts the user will be placed 340 pixels away from the left screen.
            player.rect.x = 340
            # After the player will then be shifted upwards
            player.rect.y = 200

            # we want to add the player to the sprite list groups since this contains all sprites.
            active_sprite_list.add(player)

            
            # This draws the player health bar.
            draw_healthBar(screen, 5, 5, player.health)
            draw_lives(screen, 90, 5, player.life, heartImg)
            # Go ahead and update the screen with what we've drawn.
               # Update items in the level

        if index == 8:
            level2()
            player.go_right()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT and player.change_x < 0:
            #         player.stop()
            #     if event.key == pygame.K_RIGHT and player.change_x > 0:
            #         player.stop()
            # If the player gets near the right side, shift the world left (-x)
            if player.rect.x >= 240:
                diff = player.rect.x - 240
                player.rect.x = 240
                current_level.shift_worldX(-diff)
            
            if player.rect.y <= 0:
                diff = player.rect.y
                player.rect.y = 0
                current_level.shift_worldY(-diff)
            
            if player.rect.y >= 400:
                diff = player.rect.y - 400
                player.rect.y = 400
                current_level.shift_worldY(-diff)
            
 
            hit = pygame.sprite.spritecollide(player, current_level.enemy_sprite, False)
            for hits in hit:
                # if (player.touchingGround == False):
                #     hits.kill()
                hits.jump()
                player.health -= 1
                # #player.jump()
                if (player.health <= 0): 
                    # player.rect.x = 340
                    # # After the player will then be shifted upwards
                    # player.rect.y = 200
                    current_level.shift_worldX(-current_level.world_shiftX)
                    current_level.shift_worldY(40 - current_level.world_shiftY)
                    # current_level.shift_worldY(0)
                    player.health = 100
                    player.life -= 1
                    if (player.life <= 0):
                        mainMenu()
                        player.life = 3
                        player.health = 100
                        index = 1
                    else:
                        level2()
        if index == 9:
            level3()
            screen.fill((0,0,0))
        if index == 7:
            refresh()
            screen.fill((0,0,0))
            levelSelection()
        if index == 3:
            # brodcast the settings
            for oldmembers in active_sprite_list:
                oldmembers.kill()
            screen.fill((255, 0, 0))
            buttons.add(btn3)
            active_sprite_list.add(btn3)
        #game help
        if index == 4:
            # fun features within the game
            for oldmembers in active_sprite_list:
                oldmembers.kill()
            screen.blit(helpnav1, (0,0))
            buttons.add(btn3)
            buttons.add(btn5)
            active_sprite_list.add(btn3)
            active_sprite_list.add(btn5)

            btn3.rect.x = 725
            btn5.rect.x = 570
            btn3.rect.y = 430
            btn5.rect.y = 20
        if index == 10:
            gameStore()
            screen.blit(storeImg, (0,0))
            screen.blit(playerImg, (75, 175))

            btn3.rect.x = 670
            buttons.add(btn3)
            active_sprite_list.add(btn3)
        if index == 5:
            # add the next button in here.
            for oldmembers in active_sprite_list:
                oldmembers.kill()
            screen.fill((0,0,0))
            # this is the back button. It takes you back
            buttons.add(btn7)
            active_sprite_list.add(btn7)
        elif index == 1:
           mainMenu()
        

        active_sprite_list.update()
        active_sprite_list.draw(screen)

        # Limit to 60 frames per second
        clock.tick(60)
        
       
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
