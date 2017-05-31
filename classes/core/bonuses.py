import pygame
import classes.core.settings as settings
import abc
class Bonus(pygame.sprite.Sprite):
    def __init__(self,name,speed,img,sound,x,y):
        super().__init__()
        self.name = name
        self.speed = speed
        self.img = self.img = pygame.image.load(img)
        self.sound = sound
        self.width = 33
        self.height = 33
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        settings.WINDOW.blit(self.img, self.rect)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > settings.WINDOW_HEIGHT:
            settings.BONUSES_LIST.remove(self)
            self.kill()

    #bonus action
    def action(self, ship):
        pass

class SpeedUp(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)

    def action(self,ship):
        ship.speed+=1

class BulletUp(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)

    def action(self,ship):
        ship.max_bullets+=1

class Life(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)

    def action(self,ship):
        ship.lives+=1

class Multix2(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)

    def action(self,ship):
        settings.MULTIPLIER = 2

class DoubleShoot(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)

    def action(self,ship):
        ship.weapon = settings.LIST_OF_WEAPONS[1]

class TripleShoot(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)

    def action(self,ship):
        ship.weapon = settings.LIST_OF_WEAPONS[2]

class QuadShoot(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)

    def action(self,ship):
        ship.weapon = settings.LIST_OF_WEAPONS[3]

class SuperTripleShoot(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
    def action(self,ship):
        ship.weapon = settings.LIST_OF_WEAPONS[4]

class Money10(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
    def action(self,ship):
        ship.money += 10

class Money20(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
    def action(self,ship):
        ship.money += 20

class Money50(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
    def action(self,ship):
        ship.money += 50

class Money100(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
    def action(self,ship):
        ship.money += 100

class Money200(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
    def action(self,ship):
        ship.money += 200

class Shield(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
    def action(self,ship):
        ship.godmode(10)