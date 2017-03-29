import classes.core.enemies as enemies

LIST_OF_LEVELS = []


class Level:
    def __init__(self, number_of_enemies, time, number_of_bonuses_ratio):
        self.number_of_enemies = number_of_enemies
        self.time = time
        self.number_of_bonuses_ratio = number_of_bonuses_ratio


class Level1(Level):
    def __init__(self):
        super().__init__(1, 1, 1)
    list_of_enemies = []
    enemy = enemies.Enemy1()
    list_of_enemies.append(enemy)
    # for i in range(super.time):
    #     list_of_enemies.append()


LIST_OF_LEVELS.append(Level1())
