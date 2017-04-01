import classes.core.enemies as enemies
import classes.core.settings as settings



class Level:
    def __init__(self, number_of_enemies, time, number_of_bonuses_ratio):
        self.number_of_enemies = number_of_enemies
        self.time = time
        self.number_of_bonuses_ratio = number_of_bonuses_ratio


class Level1(Level):
    def __init__(self):
        super().__init__(1, 1, 1)
    list_of_enemies = []
    x = int(800 / 2)
    y = 0
    ls = []
    offset = 0
    flag = 'right'
    for i in range(300):
        ls.append((x, y))
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
    list_of_enemies.append(enemies.Enemy1(ls[0][0], ls[0][1],100,100))
    list_of_enemies.append(enemies.Enemy1(ls[0][0], ls[0][1],300,100))
    list_of_enemies.append(enemies.Enemy1(ls[0][0], ls[0][1],500,100))
    # for i in range(super.time):
    #     list_of_enemies.append()



settings.LIST_OF_LEVELS.append(Level1())
