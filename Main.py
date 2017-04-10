import pygame
from pygame.locals import *
import time
import sys
import os
import random
import classes.core.ship as ships
import classes.core.settings as settings
import classes.core.enemies as enemies
import classes.core.levels as levels
import classes.core.bonuses as bonuses
import classes.core.drawer as drawer
pygame.init()

pygame.display.set_caption('Alien Shooter')
LEVEL_COUNTER = -1
CURRENT_LEVEL = settings.LIST_OF_LEVELS[LEVEL_COUNTER]
# R G B colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = settings.CLOCK

ship = ships.Ship()


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text, x, y, size = 24):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    settings.WINDOW.blit(TextSurf, TextRect)


def drawImg(x, y):
    settings.WINDOW.blit(ship.img, (x, y))


def gameLoop():
    global SCORE
    SCORE = 0
    xChange = 0
    LOOP = 0
    gameExit = False
    gameOver = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

            if event.type == KEYDOWN:
                if event.key == K_LEFT and ship.x - ship.speed > 0:
                    xChange = -ship.speed
                elif event.key == K_RIGHT and ship.x + ship.speed < settings.WINDOW_WIDTH - settings.SHIP_WIDTH:
                    xChange = ship.speed
                elif event.key == K_SPACE:
                    ship.shot()

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    xChange = 0
        if len(settings.LIST_OF_ENEMIES) == 0:
            global LEVEL_COUNTER
            LEVEL_COUNTER+=1
        if not settings.LIST_OF_LEVELS[0].initialized and len(settings.LIST_OF_ENEMIES) == 0:
            settings.LIST_OF_LEVELS[0].start()
        ship.x += xChange
        drawer.start()
        drawImg(ship.x, ship.y)
        for bullet in ship.bullets:
            settings.WINDOW.blit(ship.weapon.img, (bullet.x, bullet.y))
            bullet.y -= ship.weapon.speed
            if bullet.y < 0:
                ship.bullets.remove(bullet)
            for enemy in settings.LIST_OF_ENEMIES:
                if bullet.y < enemy.y + enemy.height and bullet.y > enemy.y:
                    if bullet.x > enemy.x and bullet.x < enemy.x + enemy.width:
                        settings.LIST_OF_ENEMIES.remove(enemy)
                        settings.EXPLOSION_LIST.append([(enemy.x, enemy.y), settings.EXPLOSION_TIME])
                        settings.BONUSES_LIST.append(bonuses.Test_bonus(enemy.x, enemy.y))
                        try:
                            ship.bullets.remove(bullet)
                        except ValueError:
                            print()

                        SCORE += 100

        for bullet in settings.LIST_OF_ENEMY_BULLETS:
            settings.WINDOW.blit(ship.weapon.img, (bullet.x, bullet.y))
            if bullet.y + 10 >= ship.y and bullet.y <= ship.y + 62:
                if bullet.x + 10 >= ship.x and bullet.x + 10 <= ship.x + 33:
                    settings.LIST_OF_ENEMY_BULLETS.remove(bullet)
                    if settings.LIVES > 0:
                        settings.LIVES -= 1
                    elif settings.LIVES <= 0:
                        gameOver = True
            bullet.y += 1

        for bonus in settings.BONUSES_LIST:
            settings.WINDOW.blit(bonus.img, (bonus.x, bonus.y))
            bonus.y += 1
            if (bonus.y) == 0:
                settings.BONUSES_LIST.remove(bonus)


        for explosion in settings.EXPLOSION_LIST:
            settings.WINDOW.blit(settings.EXPLOSION_IMG, explosion[0])
            explosion[1] -= 1
            if (explosion[1]) == 0:
                settings.EXPLOSION_LIST.remove(explosion)

        message_display("Score: " + str(SCORE), (settings.WINDOW_WIDTH - 100), (settings.WINDOW_HEIGHT - 570))
        message_display("Lives: " + str(settings.LIVES), (settings.WINDOW_WIDTH - 100), (settings.WINDOW_HEIGHT - 540))

        if gameOver == True:
            message_display("Game over", (settings.WINDOW_WIDTH / 2), (settings.WINDOW_HEIGHT / 2), 68)

        if ship.x > settings.WINDOW_WIDTH - settings.SHIP_WIDTH or ship.x < 0:
            xChange = 0

        pygame.display.update()

        if gameOver == True:
            time.sleep(3)
            gameOver = False

        clock.tick(settings.CLOCK_RATE)

        if len(settings.LIST_OF_ENEMIES) > 0:
            SCORE += settings.MULTIPLIER


gameLoop()
pygame.quit()
quit()
