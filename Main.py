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

pygame.init()

pygame.display.set_caption('Alien Shooter')
LEVEL_COUNTER = 0
CURRENT_LEVEL = levels.LIST_OF_LEVELS[LEVEL_COUNTER]
# R G B colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

ship = ships.Ship()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 48)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((settings.WINDOW_WIDTH - 100),(settings.WINDOW_HEIGHT - 550))
    settings.WINDOW.blit(TextSurf, TextRect)


def drawImg(x, y):
    settings.WINDOW.blit(ship.img, (x, y))


def gameLoop():
    global SCORE
    SCORE = 0
    xChange = 0

    gameExit = False

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

        ship.x += xChange

        settings.WINDOW.fill(black)
        drawImg(ship.x, ship.y)
        for bullet in ship.bullets:
            settings.WINDOW.blit(ship.weapon.img, (bullet.x, bullet.y))
            bullet.y-=ship.weapon.speed
            if bullet.y < 0:
                ship.bullets.remove(bullet)
            for enemy in CURRENT_LEVEL.list_of_enemies:
                if bullet.y < enemy.y + enemy.height and bullet.y > enemy.y:
                    if bullet.x > enemy.x and bullet.x < enemy.x + enemy.width:
                        CURRENT_LEVEL.list_of_enemies.remove(enemy)
                        ship.bullets.remove(bullet)
                        SCORE += 100

        for enemy in CURRENT_LEVEL.list_of_enemies:
            settings.WINDOW.blit(enemy.img, (enemy.x, enemy.y))
            enemy.move()

        message_display(str(SCORE))

        if ship.x > settings.WINDOW_WIDTH - settings.SHIP_WIDTH or ship.x < 0:
            xChange = 0

        pygame.display.update()
        clock.tick(120)


gameLoop()
pygame.quit()
quit()
