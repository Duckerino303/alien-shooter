import pygame

class Bonus(pygame.sprite.Sprite):
    def __init__(self,name,speed,img,sound,x,y):
        super().__init__()
        self.name = name
        self.speed = speed
        self.img = self.img = pygame.image.load(img)
        self.sound = sound
        self.width = 33
        self.height = 33
        self.x = x
        self.y = y

    def draw(self,surface):
        surface.blit(self.img, self.rect)

class Test_bonus(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
