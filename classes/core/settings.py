import pygame

CLOCK_RATE = 60
CLOCK = pygame.time.Clock()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

SHIP_WIDTH = 33
SHIP_HEIGHT = 62
SCORE = 0

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

EXPLOSION_IMG = pygame.image.load('resources/images/explosion2.png')
BACKGROUND_IMG = pygame.image.load('resources/images/background.jpg')
COLUMN_IMG = pygame.image.load('resources/images/SidePanel.png')

SHIP_IMG = pygame.image.load('resources/images/ship.png')
SHIP_GOD_IMG =pygame.image.load('resources/images/ship-god.png')

EXPLOSION_LIST = []
EXPLOSION_TIME = 15
LIST_OF_EXPLOSIONS = pygame.sprite.Group()

BONUSES_LIST = pygame.sprite.Group()

CURRENT_WEAPON = 0
LIST_OF_WEAPONS = []

LEVEL_WIN = True
LEVEL_COUNTER = -1
GAME_OVER = False
BULLETS = pygame.sprite.Group()

LIST_OF_LEVELS = []

LIST_OF_ENEMY_BULLETS = pygame.sprite.Group()
ENEMY_BULLET_SPEED = 0

LIST_OF_ENEMIES = pygame.sprite.Group()
ENEMIES_KILLED = 0
ENEMY_BULLET = pygame.image.load('resources/images/enemy-weapon.png')
BOSS_HP = 1000

MULTIPLIER = 1

