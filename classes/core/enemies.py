import pygame
import random
import classes.core.settings as settings
class Enemy:
    def __init__(self, speed, damage, hp, img, sound, x, y):
        self.speed = speed
        self.damage = damage
        self.hp = hp
        self.img = pygame.image.load(img)
        self.sound = sound
        self.width = 33
        self.height = 33
        self.x = x
        self.y = y
        self.start = self.x, self.y
        self.radius = random.randint(15,45)
        if self.radius <=30:
            self.direction = 'right'
        else:
            self.direction = 'left'

    def move(self):
        if self.direction == 'right':
            self.x += 1
            if self.x > self.start[0] + self.radius:
                self.direction = 'left'
        if self.direction == 'left':
            self.x -= 1
            if self.x < self.start[0] - self.radius:
                self.direction = 'right'


class Enemy1(Enemy):
    def __init__(self,x,y):
        super().__init__(1, 1, 1, 'resources/images/enemy1.png', None, x, y)
