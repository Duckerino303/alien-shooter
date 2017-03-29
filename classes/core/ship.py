import pygame
import classes.core.weapons as weapons
import classes.core.settings as settings
class Ship:
    def __init__(self):
        x = (settings.WINDOW_WIDTH * 0.45)
        y = (settings.WINDOW_HEIGHT - settings.SHIP_HEIGHT - 1)
        self.img = pygame.image.load('resources/images/ship.png')
        self.hp = 100
        self.speed = 5
        self.bullet_speed = 50
        self.weapon = weapons.list_of_weapons[0]
