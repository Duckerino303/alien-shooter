import pygame


class Enemy:
    def __init__(self, speed, damage, hp, img, sound):
        self.speed = speed
        self.damage = damage
        self.hp = hp
        self.img = pygame.image.load(img)
        self.sound = sound
        self.x = 0
        self.y = 0


class Enemy1(Enemy):
    def __init__(self):
        super().__init__(1, 1, 1, 'resources/images/enemy1.png', None)
