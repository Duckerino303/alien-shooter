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
        print('startowanie levelu')
        settings.LEVEL_WIN = False
        thread = threading.Thread(target=self.init_enemy_moves)
        thread.start()
        self.initialized = True
        thread = threading.Thread(target=self.spawn)
        thread.start()

    def spawn(self):
        pass


class Level1(Level):
    def __init__(self):
        super().__init__(1, 1, 1)

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
        time.sleep(5)
        print('Level 1, spawnowanie przeciwnikow')
        for i in range(1,8):
            for j in range (1,3):
                settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[0][0], self.moves_list[0][1], i*100, j*100,0,150))
                time.sleep(0.5)


class Level2(Level):
    def __init__(self):
        super().__init__(1, 1, 1)

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
        time.sleep(5)
        for i in range(1,8):
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[1][0], self.moves_list[1][1], i*100, 75, 0,250))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[250][0], self.moves_list[250][1], i*100, 150, 250, 500))
            time.sleep(0.3)
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[1][0], self.moves_list[1][1], i*100, 225,0,250))
            settings.LIST_OF_ENEMIES.add(enemies.Enemy1(self.moves_list[250][0], self.moves_list[250][1], i*100, 290,250,500))
            time.sleep(0.5)