import pygame
from pygame.locals import *
import sys
import classes.core.ship as ships
import classes.core.settings as settings
import classes.core.levels as levels
import random
import classes.core.weapons as weapons
pygame.init()
pygame.display.set_caption('Alien Shooter')
# R G B colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = settings.CLOCK

ship = ships.Ship()
ship.rect.centerx = settings.WINDOW_WIDTH // 2
ship.rect.bottom = settings.WINDOW_HEIGHT
LEVEL_COUNTER = -1
def initialiseGame():
    #adding weapons
    settings.LIST_OF_WEAPONS.append(weapons.Weapon('Single shot',1,3,'resources/images/single-shot.png'))

    #adding levels
    settings.LIST_OF_LEVELS.append(levels.Level1())
    settings.LIST_OF_LEVELS.append(levels.Level2())

    #adding first weapon
    ship.weapon = settings.LIST_OF_WEAPONS[0]

initialiseGame()
CURRENT_LEVEL = settings.LIST_OF_LEVELS[LEVEL_COUNTER]

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 24)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((settings.WINDOW_WIDTH - 100), (settings.WINDOW_HEIGHT - 570))
    settings.WINDOW.blit(TextSurf, TextRect)


def gameLoop():
    SCORE = 0
    gameExit = False
    gameOver = False


    while not gameExit:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            else:
                ship.react(event)
        settings.WINDOW.blit(settings.BACKGROUND_IMG,(0,0))

        ship.update()
        ship.draw()

        #drawing bullets
        for bullet in settings.BULLETS:
            bullet.update()
            bullet.draw()
            hit_group = pygame.sprite.spritecollide(bullet, settings.LIST_OF_ENEMIES, False)
            for enemy in hit_group:
                enemy.hit(ship.weapon.dmg)
                bullet.kill()
        for bullet in settings.LIST_OF_ENEMY_BULLETS:
            bullet.update()
            bullet.draw()

        #checking if you pass the level:
        if not settings.LIST_OF_ENEMIES and settings.LEVEL_WIN:
            global LEVEL_COUNTER
            LEVEL_COUNTER+=1
            if LEVEL_COUNTER < len(settings.LIST_OF_LEVELS):
                CURRENT_LEVEL = settings.LIST_OF_LEVELS[LEVEL_COUNTER]
                CURRENT_LEVEL.start()
            else:
                print('Wygrałeś grę')

        #rysowanie przeciwnikow
        for enemy in settings.LIST_OF_ENEMIES:
            enemy.draw()
            if not enemy.allocated:
                enemy.initialise(LEVEL_COUNTER)
            elif not enemy.initialise_allocated:
                enemy.go_to_final_position()
            elif enemy.attack_flag:
                enemy.attack()
            else:
                enemy.move()
            if random.randint(1, 1000) < 5:
                enemy.shoot()

        #drawing explosions
        for explosion in settings.LIST_OF_EXPLOSIONS:
            if explosion.counter == 0:
                explosion.kill()
            settings.WINDOW.blit(settings.EXPLOSION_IMG,(explosion.rect.x,explosion.rect.y))
            explosion.counter -= 1

        #drawing available bonuses
        for bonus in settings.BONUSES_LIST:
            bonus.update()
            bonus.draw()
            #checking if player collected bonus
            if pygame.sprite.collide_rect(ship, bonus):
                bonus.action()
                bonus.kill()


        pygame.display.flip()
        clock.tick(settings.CLOCK_RATE)
gameLoop()
pygame.quit()
quit()
