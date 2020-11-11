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

import constants
import levels

from player import Player
from enemy import Enemy
from voter_mail import PowerUp

def draw_healthBar(surf, x, y, pct):
    if pct < 0:
        pct = 0

    length = 100
    height = 10
    outline = pygame.Rect(x, y, length, height)
    pygame.draw.rect(surf, (0, 255, 0), (x, y, pct, 10))
    pygame.draw.rect(surf, (255, 255, 255),outline, 2)
    
def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    pygame.display.set_caption("Team Project")

    # Create the player
    player = Player()
    #mob = Enemy()
    
    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    # We add all the sprites in a group the reason for this is so that we can check for
    # collision between different groups of sprites.
    active_sprite_list = pygame.sprite.Group()
    # The mob group. The player can interact with the mob group.
    mob_list = pygame.sprite.Group()
    # The power up group. The player interacts with the powerups because they are in a group.
    powerUp_list = pygame.sprite.Group()
    player.level = current_level

    # When the game starts the user will be placed 340 pixels away from the left screen.
    player.rect.x = 240
    # After the player will then be shifted upwards
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height - 200

    # we want to add the player to the sprite list groups since this contains all sprites.
    active_sprite_list.add(player)
    #active_sprite_list.add(mob)
    for i in range(10):
        m = Enemy()
        m.level = current_level
        active_sprite_list.add(m)
        mob_list.add(m)

    # powers up in the level
    for power_up in range(10):
        p = PowerUp()
        p.level = current_level
        active_sprite_list.add(p)
        powerUp_list.add(p)
        
    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_LEFT:
            #        player.go_left()
            #    if event.key == pygame.K_RIGHT: 
            player.go_right()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        
        # check if the player collides with enemy either in here or in the next code.
        enemy_hit_list = pygame.sprite.spritecollide(player, mob_list, False, pygame.sprite.collide_mask)
        for hello in enemy_hit_list:
            # This code puts the player on top of the enemy slime
            # player.rect.y += -hello.rect.y // 30

            # this code makes the player bounce if they hit a slime
            # check to see if the player was previously touching the ground
            if player.rect.y >= constants.SCREEN_HEIGHT - player.rect.height and player.change_y >= 0:
                player.health -= 10
                player.jump()   # if they were then deduct health and jump
            else: # else just jump and kill slime
                player.jump()
                hello.kill()

            player.jump()

            if player.health <= 0:
               player.life -= 1
               player.health = 100
               
            if player.life <= 0:
                    player.kill()

                
        # check to see if the player collides with power ups
        powerup_hit = pygame.sprite.spritecollide(player, powerUp_list, False, pygame.sprite.collide_mask)
        for hit in powerup_hit:
            # player.health += 20
            # if player.health >= 100:
            #     player.health = 100
            hit.kill()
        # Update the player.
        active_sprite_list.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 240:
            diff = player.rect.x - 240
            player.rect.x = 240
            current_level.shift_world(-diff)
            for right in mob_list:
                right.rect.x += -diff
            for new_right in powerUp_list:
                new_right.rect.x += -diff
            
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
            for left in mob_list:
                left.rect.x += diff
            for new_left in powerUp_list:
                new_left.rect.x += diff


        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
      
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)
        
        # Update items in the level
        current_level.update()

        # This draws the player health bar.
        draw_healthBar(screen, 5, 5, player.health)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
