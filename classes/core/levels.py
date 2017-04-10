import classes.core.enemies as enemies
import classes.core.settings as settings
import threading
import time



class Level:
    def __init__(self, number_of_enemies, time, number_of_bonuses_ratio):
        self.number_of_enemies = number_of_enemies
        self.time = time
        self.number_of_bonuses_ratio = number_of_bonuses_ratio

    def start(self):
        self.init_enemy_moves()
        self.initialized = True
        thread = threading.Thread(target=self.spawn)
        thread.start()

    def spawn(self):
        pass



class Level1(Level):
    def __init__(self):
        super().__init__(1, 1, 1)
        self.ls = []
        self.initialized = False
    def init_enemy_moves(self):
        x = int(settings.WINDOW_WIDTH / 2)
        y = -10
        offset = 0
        flag = 'right'
        for i in range(300):
            self.ls.append((x, y))
            y += 1
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
    # for i in range(super.time):
    #     list_of_enemies.append()



    def spawn(self):
        settings.LIST_OF_ENEMIES.append(enemies.Enemy1(self.ls[0][0], self.ls[0][1], 100, 100))
        time.sleep(1)
        settings.LIST_OF_ENEMIES.append(enemies.Enemy1(self.ls[0][0], self.ls[0][1], 300, 100))
        time.sleep(1)
        settings.LIST_OF_ENEMIES.append(enemies.Enemy1(self.ls[0][0], self.ls[0][1], 500, 100))
        time.sleep(1)
        settings.LIST_OF_ENEMIES.append(enemies.Enemy1(self.ls[0][0], self.ls[0][1], 100, 200))
        time.sleep(1)
        settings.LIST_OF_ENEMIES.append(enemies.Enemy1(self.ls[0][0], self.ls[0][1], 300, 200))
        time.sleep(1)
        settings.LIST_OF_ENEMIES.append(enemies.Enemy1(self.ls[0][0], self.ls[0][1], 500, 200))

settings.LIST_OF_LEVELS.append(Level1())
