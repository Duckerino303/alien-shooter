import classes.core.enemies as enemies
import classes.core.settings as settings
import threading
import time



class Level:
    def __init__(self, number_of_enemies, time, number_of_bonuses_ratio):
        self.number_of_enemies = number_of_enemies
        self.time = time
        self.number_of_bonuses_ratio = number_of_bonuses_ratio
        self.moves_list = []
        self.initialized = False

    def start(self):
        settings.ENEMIES_KILLED = 0
        print('startowanie levelu')
        settings.LEVEL_WIN = False
        thread = threading.Thread(target=self.init_enemy_moves)
        thread.start()
        self.initialized = True
        thread = threading.Thread(target=self.spawn)
        thread.start()

    def spawn(self):
        pass

    def init_enemy_moves(self):
        pass

class Level1(Level):
    def __init__(self):
        super().__init__(14, 1, 1)

    def init_enemy_moves(self):
        print('inicializacja ruchow przeciwnikow')
        x = int(settings.WINDOW_WIDTH / 2)
        y = -10
        offset = 0
        flag = 'right'
        for i in range(150):
            self.moves_list.append((x, y))
            y += 2
            if (offset == 10):
                flag = 'left'
            if (offset == -10):
                flag = 'right'
            if (flag == 'right'):
                x += 1
                offset += 1
            if (flag == 'left'):
                x -= 1
                offset -= 1

    def spawn(self):
        #time.sleep(5)
        print('Level 1, spawnowanie przeciwnikow')
        for i in range(1,8):
            for j in range (1,3):
                settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[0][1], i*100, j*100,0,150))
                time.sleep(0.5)

class Level2(Level):
    def __init__(self):
        super().__init__(28, 1, 1)

    def init_enemy_moves(self):
        print('level 2 inicializacja ruchwo przeciwnikow')
        y = -10
        x1 = int(settings.WINDOW_WIDTH / 10)
        x2 = int(settings.WINDOW_HEIGHT/10 * 12)
        for i in range(250):
            self.moves_list.append((x1, y))
            y += 2
        y = -10
        for i in range(250):
            self.moves_list.append((x2, y))
            y += 2

    def spawn(self):
        #time.sleep(5)
        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[1][1], i*100, 75, 0,250))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[250][0], self.moves_list[250][1], i*100, 150, 250, 500))
            time.sleep(0.3)
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[1][1], i*100, 225,0,250))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[250][0], self.moves_list[250][1], i*100, 290,250,500))
            time.sleep(0.5)

class Level3(Level):
    def __init__(self):
        super().__init__(20, 1, 1)

    def init_enemy_moves(self):
        print('level 3 inicializacja ruchwo przeciwnikow')
        y = -10
        x = 0
        for i in range(600):
            self.moves_list.append((x, y))
            y+=0.5
            x+=4
            if x >= settings.WINDOW_WIDTH:
                x = 0

    def spawn(self):
        #time.sleep(5)
        y = 75
        x = 0
        for i in range(1,21):
            x+=1
            if i%7 == 0:
                y+=75
                x = 1
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[0][1], x*100, y, 0,600))
            time.sleep(0.4)

class Level4(Level):
    def __init__(self):
        super().__init__(21, 1, 1)

    def init_enemy_moves(self):
        print('level 4 inicializacja ruchwo przeciwnikow')
        y = -10
        x1 = int(settings.WINDOW_WIDTH / 10)
        x2 = int(settings.WINDOW_WIDTH / 2)
        x3 = int(settings.WINDOW_HEIGHT/10 * 12)
        for i in range(190):
            self.moves_list.append((x1, y))
            y+=3
        y = -10
        for i in range(190):
            self.moves_list.append((x2, y))
            y+=3
        y = -10
        for i in range(190):
            self.moves_list.append((x3, y))
            y+=3

    def spawn(self):
        #time.sleep(5)
        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[0][1], i*100, 75, 0, 190))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[190][0], self.moves_list[190][1], i*100, 150, 190, 380))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[380][0], self.moves_list[380][1], i*100, 225, 380, 570))
            time.sleep(0.4)
        print(len(settings.LIST_OF_ENEMIES))

class Level5(Level):
    def __init__(self):
        super().__init__(24, 1, 1)

    def init_enemy_moves(self):
        print('level 5 inicializacja ruchwo przeciwnikow')
        y = settings.WINDOW_HEIGHT + 10
        x1 = int(settings.WINDOW_WIDTH / 10)
        x2 = int(settings.WINDOW_HEIGHT/10 * 12)
        for i in range(250):
            self.moves_list.append((x1, y))
            y -= 3
        y = settings.WINDOW_HEIGHT + 10
        for i in range(250):
            self.moves_list.append((x2, y))
            y -= 3
        y = -10
        x = settings.WINDOW_WIDTH/2
        for i in range(250):
            self.moves_list.append((x, y))
            y += 2

    def spawn(self):
        #time.sleep(5)
        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[1][1], i*100, 75, 0,250))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[250][0], self.moves_list[250][1], i*100, 150, 250, 500))
            time.sleep(0.3)

        time.sleep(3)

        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[500][0], self.moves_list[500][1], i*100, 225, 500,750))
            time.sleep(0.3)

        time.sleep(3)

        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[500][0], self.moves_list[500][1], i*100, 290,500,750))
            time.sleep(0.3)

class Level6(Level):
    def __init__(self):
        super().__init__(28, 1, 1)

    def init_enemy_moves(self):
        print('level 6 inicializacja ruchwo przeciwnikow')
        y = -10
        x1 = int(settings.WINDOW_WIDTH / 10)
        x2 = int(settings.WINDOW_HEIGHT/10 * 12)
        for i in range(250):
            self.moves_list.append((x1, y))
            y += 3
        y = -10
        for i in range(250):
            self.moves_list.append((x2, y))
            y += 3

    def spawn(self):
        #time.sleep(5)
        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[1][1], i*100, 75, 0,250))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[250][0], self.moves_list[250][1], i*100, 150, 250, 500))
            time.sleep(0.3)
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[1][1], i*100, 225,0,250))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[250][0], self.moves_list[250][1], i*100, 290,250,500))
            time.sleep(0.5)

class Level7(Level):
    def __init__(self):
        super().__init__(20, 1, 1)

    def init_enemy_moves(self):
        print('level 7 inicializacja ruchwo przeciwnikow')
        y = -10
        x = 0
        for i in range(600):
            self.moves_list.append((x, y))
            y+=0.5
            x+=4
            if x >= settings.WINDOW_WIDTH:
                x = 0

    def spawn(self):
        #time.sleep(5)
        y = 75
        x = 0
        for i in range(1,21):
            x+=1
            if i%7 == 0:
                y+=75
                x = 1
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[0][1], x*100, y, 0,600))
            time.sleep(0.4)

class Level8(Level):
    def __init__(self):
        super().__init__(21, 1, 1)

    def init_enemy_moves(self):
        print('level 8 inicializacja ruchwo przeciwnikow')
        y = -10
        x1 = int(settings.WINDOW_WIDTH / 10)
        x2 = int(settings.WINDOW_WIDTH / 2)
        x3 = int(settings.WINDOW_HEIGHT/10 * 12)
        for i in range(190):
            self.moves_list.append((x1, y))
            y+=3
        y = -10
        for i in range(190):
            self.moves_list.append((x2, y))
            y+=3
        y = -10
        for i in range(190):
            self.moves_list.append((x3, y))
            y+=3

    def spawn(self):
        #time.sleep(5)
        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[0][1], i*100, 75, 0, 190))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[190][0], self.moves_list[190][1], i*100, 150, 190, 380))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[380][0], self.moves_list[380][1], i*100, 225, 380, 570))
            time.sleep(0.4)
        print(len(settings.LIST_OF_ENEMIES))

class Level9(Level):
    def __init__(self):
        super().__init__(24, 1, 1)

    def init_enemy_moves(self):
        print('level 9 inicializacja ruchwo przeciwnikow')
        y = settings.WINDOW_HEIGHT + 10
        x1 = int(settings.WINDOW_WIDTH / 10)
        x2 = int(settings.WINDOW_HEIGHT/10 * 12)
        for i in range(250):
            self.moves_list.append((x1, y))
            y -= 3
        y = settings.WINDOW_HEIGHT + 10
        for i in range(250):
            self.moves_list.append((x2, y))
            y -= 3
        y = -10
        x = settings.WINDOW_WIDTH/2
        for i in range(250):
            self.moves_list.append((x, y))
            y += 2

    def spawn(self):
        #time.sleep(5)
        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[1][1], i*100, 75, 0,250))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[250][0], self.moves_list[250][1], i*100, 150, 250, 500))
            time.sleep(0.3)

        time.sleep(3)

        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[500][0], self.moves_list[500][1], i*100, 225, 500,750))
            time.sleep(0.3)

        time.sleep(3)

        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[500][0], self.moves_list[500][1], i*100, 290,500,750))
            time.sleep(0.3)

class Level10(Level):
    def __init__(self):
        super().__init__(1, 1, 1)

    def init_enemy_moves(self):
        print('inicializacja ruchow przeciwnikow')
        x = int(settings.WINDOW_WIDTH / 2 -125)
        y = -10
        for i in range(150):
            self.moves_list.append((x, y))
            y += 2


    def spawn(self):
        #time.sleep(5)
        settings.LIST_OF_ENEMIES.add(enemies.Boss(self.moves_list[0][0], self.moves_list[0][1], settings.WINDOW_WIDTH/2 - 125, 0,0,150))