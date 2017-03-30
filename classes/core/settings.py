import pygame
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
SHIP_WIDTH = 33
SHIP_HEIGHT = 62
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
EXPLOSION_IMG = pygame.image.load('resources/images/explosion.png')
EXPLOSION_LIST = []
EXPLOSION_TIME = 15