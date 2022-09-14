import random


class WarriorsStats:
    health = 100

    def __init__(self, name):
        self.name = name


def fight(first, two):
    while True:
        index = random.randint(0, 1)
        if index == 1:
            if damage_deal(first):
                break
        else:
            if damage_deal(two):
                break


def damage_deal(number):
    if number.health > 0:
        number.health -= 20
        print('Воин по имени {}, получил урон, его здоровье теперь {}'.format(
            number.name, number.health))
    else:
        print('Воин по имени {} погиб.'.format(number.name))
        return True


warrior_one = WarriorsStats('Боб')
warrior_two = WarriorsStats('не Боб')

fight(warrior_one, warrior_two)
