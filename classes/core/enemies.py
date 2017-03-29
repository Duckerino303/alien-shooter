import pygame


class Enemy:
    def __init__(self, speed, damage, hp, img, sound, x, y):
        self.speed = speed
        self.damage = damage
        self.hp = hp
        self.img = pygame.image.load(img)
        self.sound = sound
        self.x = x
        self.y = y
        self.start = self.x, self.y
        self.direction = 'right'

    def move(self):
        if self.direction == 'right':
            self.x += 1
            if self.x > self.start[0] + 45:
                self.direction = 'left'
        if self.direction == 'left':
            self.x -= 1
            if self.x < self.start[0] - 45:
                self.direction = 'right'


class Enemy1(Enemy):
    def __init__(self):
        super().__init__(1, 1, 1, 'resources/images/enemy1.png', None, 100, 100)
