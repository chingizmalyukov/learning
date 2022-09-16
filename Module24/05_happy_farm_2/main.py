class Potato:
    states = {0: 'Детство', 1: 'Отрочество', 2: 'Юность', 3: 'Зрелость'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))


class PotatoGarden:
    potatos_ready = 0

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        if len(self.potatoes):
            print('Картошка прорастает!\n')
            for potato in self.potatoes:
                potato.grow()
        else:
            print('Грядка пуста!\n')

    def are_all_ripe(self):
        self.potatos_ready = 0
        if all([i_potato.is_ripe() for i_potato in self.potatoes]):
            self.potatos_ready = len(self.potatoes)
            self.potatoes.clear()
            return self.potatos_ready
        else:
            return 0

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()


class Gardener:
    garden_list = []
    harvested_potatos = 0

    def __init__(self, name):
        self.name = name

    def care(self):
        for i_garden in self.garden_list:
            i_garden.grow_all()
            self.harvested_potatos += i_garden.are_all_ripe()

    def harvested_info(self):
        print('Количество собранной картошки: {}'.format(self.harvested_potatos))


# Не очень понял что значит "ухаживать за грядкой", сделал так: при уходе за грядкой садовник собирает урожай,
# если урожай не готов, то взращивает его.
# NOTE Да, отличный подход к решению получился!

garden = PotatoGarden(5)
gardener = Gardener('Tomas')
gardener.garden_list.append(garden)

for _ in range(4):
    gardener.care()

gardener.harvested_info()
