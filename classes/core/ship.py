import pygame
import classes.core.settings as settings
import threading
import time

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = settings.SHIP_IMG
        self.rect = self.img.get_rect()
        self.move_speed = 0
        self.speed = 4
        self.lives = 3
        self.bullet_speed = 50
        self.weapon = 0
        self.max_bullets = 10
        self.god = False
        self.money = 1000

    def reset(self):
        self.rect.centerx = settings.WINDOW_WIDTH // 2
        self.rect.bottom = settings.WINDOW_HEIGHT
        threading.Thread(target=self.godmode, args=(3,)).start()

    def godmode(self, duration):
        self.god = True
        self.img = settings.SHIP_GOD_IMG
        time.sleep(duration)
        self.god = False
        self.img = settings.SHIP_IMG

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
            elif event.key == pygame.K_1:
                self.buyWeapon(1)
            elif event.key == pygame.K_2:
                self.buyWeapon(2)
            elif event.key == pygame.K_3:
                self.buyWeapon(3)
            elif event.key == pygame.K_4:
                self.buyWeapon(4)
            elif event.key == pygame.K_5:
                self.buyWeapon(5)
            elif event.key == pygame.K_6 and self.money >= 1000:
                self.lives += 1
                self.money -= 1000
            elif event.key == pygame.K_7 and self.money >= 1000:
                threading.Thread(target=self.godmode, args=(10,)).start()
                self.money -= 1000
            elif event.key == pygame.K_8 and self.money >= 100:
                self.max_bullets+=1
                self.money -= 100
            elif event.key == pygame.K_9 and self.money >= 100:
                self.speed+=1
                self.money -= 100
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and self.move_speed < 0:
                self.stop()
            if event.key == pygame.K_RIGHT and self.move_speed > 0:
                self.stop()

    def buyWeapon(self,number):
        if self.money >= settings.LIST_OF_WEAPONS[number].price:
            self.weapon = settings.LIST_OF_WEAPONS[number]
            self.money -= settings.LIST_OF_WEAPONS[number].price
            settings.CURRENT_WEAPON = number