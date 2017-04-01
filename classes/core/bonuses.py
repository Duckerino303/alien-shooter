import pygame

class Bonus:
    def __init__(self,name,speed,img,sound,x,y):
        self.name = name
        self.speed = speed
        self.img = self.img = pygame.image.load(img)
        self.sound = sound
        self.width = 33
        self.height = 33
        self.x = x
        self.y = y

class Test_bonus(Bonus):
    def __init__(self,x,y):
        super().__init__('Bonus', 1, 'resources/images/bonus_test.png', None, x, y)
