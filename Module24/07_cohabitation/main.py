import random


class Human:
    satiety = 50
    status = True
    day = 0

    def __init__(self, name, home):
        self.name = name
        self.home = home

    def eat(self):
        print('{} решает покушать'.format(self.name))
        if self.home.frig < 10:
            print('но не тут то было, еды-то нет!')
            self.shop()
        self.satiety += 20
        self.home.frig -= 20

    def work(self):
        print('{} идет работать'.format(self.name))
        self.satiety -= 20
        if self.satiety <= 0:
            print('{} УМЕРАЕТ ОТ ГОЛОДА'.format(self.name))
            self.status = False
        self.home.table += 30

    def play(self):
        print('{} принимает ответственное решение - поиграть'.format(self.name))
        self.satiety -= 10
        if self.satiety <= 0:
            print('{} УМЕРАЕТ ОТ ГОЛОДА'.format(self.name))
            self.status = False

    def shop(self):
        print('{} понимает, что нужно идти в магазин!'.format(self.name))
        if self.home.table < 50:
            print('но не тут то было, денег-то нет!')
            self.work()
        self.home.frig += 20
        self.home.table -= 20

    def action(self):
        print('{}, кол-во прожитых дней: {}, денег в доме {}, голод {}'.format(
            self.name, self.day, self.home.table, self.satiety))
        number = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.frig < 10:
            self.work()
        elif self.home.table < 50:
            self.work()
        elif number == 1:
            self.work()
        elif number == 2:
            self.eat()
        else:
            self.play()
        self.day += 1


class Home:
    frig = 50
    table = 0

    def __init__(self, home_name):
        home_name = home_name


home = Home('dom2')
petr = Human('Petr', home)
oleg = Human('Olga', home)
print('Кажется Ольга что-то скрывает...')

for day in range(1, 366):
    if not petr.status and not oleg.status:
        print('Кол-во дней которые прожили ребята: {}.'.format(day))
        break
    print('\nНачался {} день нашей стройки.'.format(day))
    if petr.status:
        petr.action()
    if oleg.status:
        oleg.action()
