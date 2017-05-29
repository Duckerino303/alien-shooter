import pygame
import classes.core.settings as settings
class Weapon(pygame.sprite.Sprite):
    def __init__(self,name, dmg=1, speed=50, img=None, sound=None, consume_bullets=1):
        super().__init__()
        self.name = name
        self.dmg = dmg
        self.speed = speed
        self.img = pygame.image.load(img)
        self.sound = sound
        self.consume_bullets = consume_bullets



class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, x, y):
        super().__init__()
        self.rect = settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        settings.WINDOW.blit(settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].img, self.rect)

    def update(self):
        self.rect.y -= settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].speed
        if self.rect.bottom < 0:
            settings.BULLETS.remove(self)
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, speed, x, y):
        super().__init__()
        self.rect = settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        settings.WINDOW.blit(settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].img, self.rect)

    def update(self):
        self.rect.y += settings.ENEMY_BULLET_SPEED
        if self.rect.bottom < 0:
            settings.BULLETS.remove(self)
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.rect =settings.EXPLOSION_IMG.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = settings.EXPLOSION_TIME