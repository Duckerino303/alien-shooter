import pygame

CLOCK_RATE = 60
CLOCK = pygame.time.Clock()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

SHIP_WIDTH = 33
SHIP_HEIGHT = 62

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

EXPLOSION_IMG = pygame.image.load('resources/images/explosion.png')
BACKGROUND_IMG = pygame.image.load('resources/images/background.jpg')
COLUMN_IMG = pygame.image.load('resources/images/column.png')

EXPLOSION_LIST = []
EXPLOSION_TIME = 15
LIST_OF_EXPLOSIONS = pygame.sprite.Group()

BONUSES_LIST = pygame.sprite.Group()

CURRENT_WEAPON = 5
LIST_OF_WEAPONS = []

LEVEL_WIN = True
LEVEL_COUNTER = -1

BULLETS = pygame.sprite.Group()

LIST_OF_LEVELS = []

LIST_OF_ENEMY_BULLETS = pygame.sprite.Group()
ENEMY_BULLET_SPEED = 0

LIST_OF_ENEMIES = pygame.sprite.Group()
ENEMIES_KILLED = 0
BOSS_HP = 1000

MULTIPLIER = 1

def reset():
    global LIST_OF_ENEMY_BULLETS, LIST_OF_ENEMIES
    LIST_OF_ENEMY_BULLETS = pygame.sprite.Group()
    LIST_OF_ENEMIES = pygame.sprite.Group()