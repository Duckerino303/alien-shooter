import pygame
import classes.core.settings as settings


class Weapon(pygame.sprite.Sprite):
    def __init__(self, name, dmg, speed, img=None, sound=None, consume_bullets=1):
        super().__init__()
        self.name = name
        self.dmg = dmg
        self.speed = speed
        self.img = pygame.image.load(img)
        self.sound = sound
        self.consume_bullets = consume_bullets
        self.price = 0

    def shoot(self, max_bullets, x, y):
        pass


class Weapon1(Weapon):
    def __init__(self):
        super().__init__('single', 1, 2, 'resources/images/single-shot.png')

    def shoot(self, max_bullets, x, y):
        if len(settings.BULLETS) < max_bullets:
            settings.BULLETS.add(Bullet(self.speed, x, y,0,1))

class Weapon2(Weapon):
    def __init__(self):
        super().__init__('double', 2, 3, 'resources/images/single-shot.png')
        self.price = 50
    def shoot(self, max_bullets, x, y):
        if len(settings.BULLETS) + 1 < max_bullets:
            settings.BULLETS.add(Bullet(self.speed, x-7, y,0,1))
            settings.BULLETS.add(Bullet(self.speed, x+7, y,0,1))

class Weapon3(Weapon):
    def __init__(self):
        super().__init__('triple', 3, 4, 'resources/images/single-shot.png')
        self.price = 150
    def shoot(self, max_bullets, x, y):
        if len(settings.BULLETS) + 2 < max_bullets:
            settings.BULLETS.add(Bullet(self.speed, x, y,0.5,1))
            settings.BULLETS.add(Bullet(self.speed, x, y,0,1))
            settings.BULLETS.add(Bullet(self.speed, x, y,-0.5,1))

class Weapon4(Weapon):
    def __init__(self):
        super().__init__('quad', 4, 5, 'resources/images/single-shot.png')
        self.price = 300
    def shoot(self, max_bullets, x, y):
        if len(settings.BULLETS) + 3 < max_bullets:
            settings.BULLETS.add(Bullet(self.speed, x-16, y,0,1))
            settings.BULLETS.add(Bullet(self.speed, x+16, y,0,1))
            settings.BULLETS.add(Bullet(self.speed, x-5, y,0,1))
            settings.BULLETS.add(Bullet(self.speed, x+5, y,0,1))

class Weapon5(Weapon):
    def __init__(self):
        super().__init__('super3', 5, 7, 'resources/images/single-shot.png')
        self.price = 500
    def shoot(self, max_bullets, x, y):
        if len(settings.BULLETS) + 2 < max_bullets:
            settings.BULLETS.add(Bullet(self.speed, x, y,0.5,1))
            settings.BULLETS.add(Bullet(self.speed, x, y,0,1))
            settings.BULLETS.add(Bullet(self.speed, x, y,-0.5,1))

class Weapon6(Weapon):
    def __init__(self):
        super().__init__('fireball', 10, 10, 'resources/images/single-shot.png')
        self.price = 1000
    def shoot(self, max_bullets, x, y):
        if len(settings.BULLETS) + 2 < max_bullets:
            settings.BULLETS.add(Bullet(self.speed, x, y,0,1))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, x, y, xchange, ychange):
        super().__init__()
        self.rect = settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.xchange = xchange
        self.ychange = ychange

    def draw(self):
        settings.WINDOW.blit(settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].img, self.rect)

    def update(self):
        self.rect.y -= self.ychange * settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].speed
        self.rect.x -= self.xchange *settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].speed
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
    def __init__(self, x, y):
        super().__init__()
        self.rect = settings.EXPLOSION_IMG.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = settings.EXPLOSION_TIME
