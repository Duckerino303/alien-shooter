import pygame
import classes.core.settings as settings
import abc
import threading
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
        super().__init__('Bonus', 2, 'resources/images/SpeedBonus.png', None, x, y)

    def action(self,ship):
        ship.speed+=1

class BulletUp(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 2, 'resources/images/BulletUpBonus.png', None, x, y)

    def action(self,ship):
        ship.max_bullets+=1

class Life(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 5, 'resources/images/LifeBonus.png', None, x, y)

    def action(self,ship):
        ship.lives+=1

class Multix2(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 2, 'resources/images/MulitplierBonus.png', None, x, y)

    def action(self,ship):
        settings.MULTIPLIER = 2

class DoubleShoot(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 3, 'resources/images/DoubleShotBonus.png', None, x, y)

    def action(self,ship):
        ship.weapon = settings.LIST_OF_WEAPONS[1]
        settings.CURRENT_WEAPON = 1

class TripleShoot(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 4, 'resources/images/TripleShotBonus.png', None, x, y)

    def action(self,ship):
        ship.weapon = settings.LIST_OF_WEAPONS[2]
        settings.CURRENT_WEAPON = 2

class QuadShoot(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 5, 'resources/images/QuadShotBonus.png', None, x, y)

    def action(self,ship):
        ship.weapon = settings.LIST_OF_WEAPONS[3]
        settings.CURRENT_WEAPON = 3

class SuperTripleShoot(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 6, 'resources/images/SuperTripleShotBonus.png', None, x, y)
    def action(self,ship):
        ship.weapon = settings.LIST_OF_WEAPONS[4]
        settings.CURRENT_WEAPON = 4

class Money10(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 2, 'resources/images/10gold.png', None, x, y)
    def action(self,ship):
        ship.money += 10

class Money20(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 3, 'resources/images/20gold.png', None, x, y)
    def action(self,ship):
        ship.money += 20

class Money50(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 4, 'resources/images/50gold.png', None, x, y)
    def action(self,ship):
        ship.money += 50

class Money100(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 5, 'resources/images/100gold.png', None, x, y)
    def action(self,ship):
        ship.money += 100

class Money200(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 6, 'resources/images/200gold.png', None, x, y)
    def action(self,ship):
        ship.money += 200

class Shield(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 6, 'resources/images/ShieldBonus.png', None, x, y)
    def action(self,ship):
        threading.Thread(target=ship.godmode, args=(10,)).start()