import pygame
from pygame.locals import *
import time
import sys
import os
import random
import classes.core.ship as ship

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Alien Shooter')

# R G B colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

ship = ship.Ship()

shipWidth = 166
shipHeight = 309


def img(x, y):
    WINDOW.blit(ship.img, (x, y))


def gameLoop():
    x = (WINDOW_WIDTH * 0.45)
    y = (WINDOW_HEIGHT * 0.45)

    xChange = 0

    shipSpeed = 5

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    xChange = -shipSpeed
                elif event.key == K_RIGHT:
                    xChange = shipSpeed

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    xChange = 0

        x += xChange

        WINDOW.fill(black)
        img(x, y)

        if x > WINDOW_WIDTH - shipWidth or x < 0:
            xChange = 0

        pygame.display.update()
        clock.tick(120)


gameLoop()
pygame.quit()
quit()
