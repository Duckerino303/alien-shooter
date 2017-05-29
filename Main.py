import pygame
from pygame.locals import *
import sys
import classes.core.ship as ships
import classes.core.settings as settings
import classes.core.levels as levels
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
def initialiseGame():
    settings.LIST_OF_LEVELS.append(levels.Level1())
initialiseGame()
LEVEL_COUNTER = 0
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
    xChange = 0
    gameExit = False
    gameOver = False
    currentLevel = 0


    while not gameExit:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            else:
                ship.react(event)
        settings.WINDOW.blit(settings.BACKGROUND_IMG,(0,0))

        ship.update()
        ship.draw()

        #rysowanie bulletow
        for bullet in settings.BULLETS:
            bullet.update()
            bullet.draw()

        for enemy in settings.LIST_OF_ENEMIES:
            enemy.draw()
            enemy.go_to_final_position()

        pygame.display.flip()
        clock.tick(settings.CLOCK_RATE)
gameLoop()
pygame.quit()
quit()
