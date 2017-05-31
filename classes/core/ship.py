import pygame
import classes.core.settings as settings
import threading
import time

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('resources/images/ship.png')
        self.rect = self.img.get_rect()
        self.move_speed = 0
        self.speed = 4
        self.lives = 3
        self.bullet_speed = 50
        self.weapon = None
        self.max_bullets = 5
        self.god = False

    def reset(self):
        self.rect.centerx = settings.WINDOW_WIDTH // 2
        self.rect.bottom = settings.WINDOW_HEIGHT
        threading.Thread(target=self.godmode, args=(3,)).start()

    def godmode(self, duration):
        self.god = True
        time.sleep(duration)
        self.god = False

    def shoot(self):
        self.weapon.shoot(self.max_bullets, self.rect.centerx -5, self.rect.top)


    def draw(self):
        settings.WINDOW.blit(self.img, self.rect)

    def move_left(self):
        self.move_speed = -1 * self.speed

    def move_right(self):
        self.move_speed = self.speed

    def stop(self):
        self.move_speed = 0


    def update(self):
        self.rect.x += self.move_speed
        if self.rect.right > settings.WINDOW_WIDTH-100:
            self.rect.right = settings.WINDOW_WIDTH-100
        if self.rect.left < 100:
            self.rect.left = 100

    def react(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left()
            elif event.key == pygame.K_RIGHT:
                self.move_right()
            elif event.key == pygame.K_SPACE:
                self.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.move_speed < 0:
                self.stop()
            if event.key == pygame.K_RIGHT and self.move_speed > 0:
                self.stop()