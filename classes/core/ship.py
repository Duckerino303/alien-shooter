import pygame
import classes.core.weapons as weapons
import classes.core.settings as settings


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        settings.LIST_OF_WEAPONS.append(weapons.Weapon('Single shot',1,3,'resources/images/single-shot.png'))
        self.img = pygame.image.load('resources/images/ship.png')
        self.rect = self.img.get_rect()
        self.hp = 100
        self.speed = 0
        self.bullet_speed = 50
        self.weapon = settings.LIST_OF_WEAPONS[0]
        self.max_bullets = 5


    def shot(self):
        if len(settings.BULLETS) < self.max_bullets:
            settings.BULLETS.add(
                weapons.Bullet(settings.LIST_OF_WEAPONS[settings.CURRENT_WEAPON].speed,self.rect.centerx -5,self.rect.top))

    def draw(self):
        settings.WINDOW.blit(self.img, self.rect)

    def move_left(self):
        self.speed = -6

    def move_right(self):
        self.speed = 6

    def stop(self):
        self.speed = 0


    def update(self):
        self.rect.x += self.speed
        if self.rect.right > settings.WINDOW_WIDTH:
            self.rect.right = settings.WINDOW_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def react(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left()
            elif event.key == pygame.K_RIGHT:
                self.move_right()
            elif event.key == pygame.K_SPACE:
                self.shot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.speed < 0:
                self.stop()
            if event.key == pygame.K_RIGHT and self.speed > 0:
                self.stop()