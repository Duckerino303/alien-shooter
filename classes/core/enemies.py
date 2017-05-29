import pygame
import random
import classes.core.settings as settings
import classes.core.weapons as weapons
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, damage, hp, img, sound, x, y, final_x, final_y):
        super().__init__()
        self.speed = speed
        self.damage = damage
        self.hp = hp
        self.img = pygame.image.load(img)
        self.sound = sound
        self.width = 33
        self.height = 33
        self.start = self.rect.x, self.rect.y
        self.final_position = final_x,final_y
        self.radius = random.randint(15,45)
        self.allocated=False
        self.initialise_allocated=False
        self.initialise_counter = 0
        if self.radius <=30:
            self.direction = 'right'
        else:
            self.direction = 'left'
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def initialise(self,level):
        ls = settings.LIST_OF_LEVELS[level].ls
        self.rect.x = ls[self.initialise_counter][0]
        self.rect.y = ls[self.initialise_counter][1]
        self.initialise_counter+=1
        if self.initialise_counter > 299:
            self.allocated = True

    def go_to_final_position(self):
        if self.rect.x < self.final_position[0]:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.rect.y < self.final_position[1]:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed
        if abs(self.final_position[0] - self.rect.x) <= 5 and  abs(self.final_position[1] - self.rect.y)<=5:
            self.initialise_allocated = True

    def move(self):
        if self.direction == 'right':
            self.rect.x += 1
            if self.rect.x > self.final_position[0] + self.radius:
                self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= 1
            if self.rect.x < self.final_position[0] - self.radius:
                self.direction = 'right'

    def shoot(self):
        settings.LIST_OF_ENEMY_BULLETS.append(weapons.Bullet(self.rect.x,self.rect.y))

    def draw(self):
        settings.WINDOW.blit(self.img, self.rect)

class Enemy1(Enemy):
    def __init__(self,x,y, final_x, final_y):
        super().__init__(1, 1, 1, 'resources/images/enemy1.png', None,x, y, final_x, final_y)
