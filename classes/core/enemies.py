import pygame
import random
import classes.core.settings as settings
import classes.core.weapons as weapons
import classes.core.bonuses as bonuses
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, damage, hp, bullet_speed, img, sound, x, y, final_x, final_y, initialise_counter, init_steps):
        super().__init__()
        self.speed = speed
        self.damage = damage
        self.hp = hp
        self.bullet_speed = bullet_speed
        self.img = pygame.image.load(img)
        self.sound = sound
        self.width = 33
        self.height = 33
        self.score = 50
        #szybkość strzału
        #docelowa pozycja
        self.final_position = final_x,final_y
        #promień w jakim może się poruszać podczas self.move()
        self.radius = random.randint(15,45)
        #czy skończył startowy ruch
        self.allocated=False
        #czy dotarł na finalną pozycje
        self.initialise_allocated=False
        #ilość kroków podczas ruchu startowego
        self.initialise_counter = initialise_counter
        #ilość kroków w ruchu startowym
        self.number_of_init_steps = init_steps
        #losowość poruszania się na boki
        if self.radius <=30:
            self.direction = 'right'
        else:
            self.direction = 'left'
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        #gdzie się respi
        self.start = x, y
        #czy obecnie atakuje
        self.attack_flag = False
        self.shoot_ratio = 5

    #start move
    def initialise(self, level):
        ls = settings.LIST_OF_LEVELS[level].moves_list
        self.rect.x = ls[self.initialise_counter][0]
        self.rect.y = ls[self.initialise_counter][1]
        self.initialise_counter+=1
        if self.initialise_counter > self.number_of_init_steps -1:
            self.allocated = True

    #after start move is going to final position
    def go_to_final_position(self):
        if self.rect.x < self.final_position[0]:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.rect.y < self.final_position[1]:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed
        if abs(self.final_position[0] - self.rect.x) <= 5 and abs(self.final_position[1] - self.rect.y)<=5:
            self.initialise_allocated = True

    #moving to the right and left, after gaining final position
    def move(self):
        if self.direction == 'right':
            self.rect.x += self.speed
            if self.rect.x > self.final_position[0] + self.radius:
                self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
            if self.rect.x < self.final_position[0] - self.radius:
                self.direction = 'right'
        attackChoice = random.randint(1,10000)
        if attackChoice < 2:
            self.attack_flag = True

    #attack, move enemy to bottom of the screen
    def attack(self):
        self.rect.y += 2*self.speed
        if self.rect.y >= settings.WINDOW_HEIGHT:
            self.rect.y = 0
            self.attack_flag = False
            self.initialise_allocated = False

    def shoot(self):
        if random.randint(1, 1000) < self.shoot_ratio:
            settings.LIST_OF_ENEMY_BULLETS.add(weapons.EnemyBullet(self.bullet_speed, self.rect.x, self.rect.y))

    def draw(self):
        settings.WINDOW.blit(self.img, self.rect)

    #it's called when you hit enemy
    def hit(self,power, level):
        self.hp -= power
        if self.hp<=0:
            bonus_chance = random.randint(0,10)
            if bonus_chance < 5:
                bonus = random.randint(0,13)
                if bonus==0:
                    settings.BONUSES_LIST.add(bonuses.SpeedUp(self.rect.x,self.rect.y))
                elif bonus==1:
                    settings.BONUSES_LIST.add(bonuses.BulletUp(self.rect.x,self.rect.y))
                elif bonus==2:
                    settings.BONUSES_LIST.add(bonuses.Life(self.rect.x,self.rect.y))
                elif bonus==3:
                    settings.BONUSES_LIST.add(bonuses.DoubleShoot(self.rect.x,self.rect.y))
                elif bonus==4:
                    settings.BONUSES_LIST.add(bonuses.TripleShoot(self.rect.x,self.rect.y))
                elif bonus==5:
                    settings.BONUSES_LIST.add(bonuses.QuadShoot(self.rect.x,self.rect.y))
                elif bonus==6:
                    settings.BONUSES_LIST.add(bonuses.SuperTripleShoot(self.rect.x,self.rect.y))
                elif bonus==7:
                    settings.BONUSES_LIST.add(bonuses.Money10(self.rect.x,self.rect.y))
                elif bonus==8:
                    settings.BONUSES_LIST.add(bonuses.Money20(self.rect.x,self.rect.y))
                elif bonus==9:
                    settings.BONUSES_LIST.add(bonuses.Money50(self.rect.x,self.rect.y))
                elif bonus==10:
                    settings.BONUSES_LIST.add(bonuses.Money100(self.rect.x,self.rect.y))
                elif bonus==11:
                    settings.BONUSES_LIST.add(bonuses.Money200(self.rect.x,self.rect.y))
                elif bonus==12:
                    settings.BONUSES_LIST.add(bonuses.Shield(self.rect.x,self.rect.y))
            settings.LIST_OF_EXPLOSIONS.add(weapons.Explosion(self.rect.x,self.rect.y))
            self.kill()
            settings.LIST_OF_ENEMIES.remove(self)
            settings.ENEMIES_KILLED += 1
            settings.SCORE += self.score * settings.MULTIPLIER
            #check if last enemy, if yes changing settings.LEVEL_WIN to true
            if len(settings.LIST_OF_ENEMIES) ==0 and settings.ENEMIES_KILLED == settings.LIST_OF_LEVELS[level].number_of_enemies:
                settings.LEVEL_WIN = True


class Enemy1(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(1, 1, 2, 10, 'resources/images/enemy1.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED = 5
class Enemy2(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(2, 2, 3, 10, 'resources/images/enemy2.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED = 5
class Enemy3(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(2, 3, 3, 10, 'resources/images/enemy3.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED = 5
class Enemy4(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(3, 4, 4, 10, 'resources/images/enemy4.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED = 5
class Enemy5(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(3, 5, 5, 10, 'resources/images/enemy5.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED = 6
class Enemy6(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(4, 6, 7, 10, 'resources/images/enemy6.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED =6
class Enemy7(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(4, 7, 8, 10, 'resources/images/enemy7.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED = 7
class Enemy8(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(4, 8, 10, 10, 'resources/images/enemy8.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED = 7
class Enemy9(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(5, 10, 2, 10, 'resources/images/enemy9.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        settings.ENEMY_BULLET_SPEED = 8



class Boss(Enemy):
    def __init__(self,x,y, final_x, final_y, initialise_counter, init_steps):
        super().__init__(3, 1, 1000, 10, 'resources/images/VS_demilich.png', None,x, y, final_x, final_y, initialise_counter, init_steps)
        self.shoot_ratio = 10
        self.score = 1000
        settings.ENEMY_BULLET_SPEED = 10
        self.radius = 200
    def shoot(self):
        if random.randint(1, 1000) < self.shoot_ratio:
            change = random.randint(1,200)
            settings.LIST_OF_ENEMY_BULLETS.add(weapons.EnemyBullet(self.bullet_speed, self.rect.x + change, self.rect.y))

    def go_to_final_position(self):
        self.rect.y -= self.speed
        if abs(self.final_position[0] - self.rect.x) <= 5 and abs(self.final_position[1] - self.rect.y)<=5:
            self.initialise_allocated = True

    def move(self):
        if self.direction == 'right':
            self.rect.x += self.speed
            if self.rect.x > self.final_position[0] + self.radius:
                self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
            if self.rect.x < self.final_position[0] - self.radius:
                self.direction = 'right'
    def hit(self,power, level):
        self.hp -= power
        settings.BOSS_HP -= power
        if self.hp<=0:
            bonus_chance = random.randint(0,10)
            if bonus_chance < 1:
                settings.BONUSES_LIST.add(bonuses.Test_bonus(self.rect.x,self.rect.y))
            settings.LIST_OF_EXPLOSIONS.add(weapons.Explosion(self.rect.x,self.rect.y))
            self.kill()
            settings.LIST_OF_ENEMIES.remove(self)
            settings.ENEMIES_KILLED += 1
            #check if last enemy, if yes changing settings.LEVEL_WIN to true
            if len(settings.LIST_OF_ENEMIES) ==0 and settings.ENEMIES_KILLED == settings.LIST_OF_LEVELS[level].number_of_enemies:
                settings.LEVEL_WIN = True