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

class Test_bonus(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)

    def action(self):
        print('Zebrałeś bonus')