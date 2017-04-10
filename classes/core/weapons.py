import pygame
class Weapon:
    def __init__(self,name, dmg=1, speed=50, img=None, sound=None, consume_bullets=1):
        self.name = name
        self.dmg = dmg
        self.speed = speed
        self.img = pygame.image.load(img)
        self.sound = sound
        self.consume_bullets = consume_bullets

list_of_weapons = []
list_of_weapons.append(Weapon('Single shot',1,3,'resources/images/single-shot.png'))

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
