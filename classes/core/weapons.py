class Weapon:
    def __init__(self,name, dmg=1, speed=50, img=None, sound=None, maxBullets = 5):
        self.name = name
        self.dmg = dmg
        self.speed = speed
        self.img = img
        self.sound = sound
        # self.maxBullets = maxBullets

list_of_weapons = []
list_of_weapons.append(Weapon('Single shot'))
