import pygame

CLOCK_RATE = 120
CLOCK = pygame.time.Clock()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

SHIP_WIDTH = 33
SHIP_HEIGHT = 62

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

EXPLOSION_IMG = pygame.image.load('resources/images/explosion.png')
BACKGROUND_IMG = pygame.image.load('resources/images/background.jpg')

EXPLOSION_LIST = []
EXPLOSION_TIME = 15

BONUSES_LIST = []

CURRENT_WEAPON = 0
LIST_OF_WEAPONS = []

BULLETS = pygame.sprite.Group()

LIST_OF_LEVELS = []

LIST_OF_ENEMY_BULLETS = []
LIST_OF_ENEMIES = pygame.sprite.Group()

MULTIPLIER = 1