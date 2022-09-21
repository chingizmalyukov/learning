class Home:
    __money = 100
    __food = 50
    __cat_food = 30
    __dirt = 0
    __food_eaten = 0
    __coats_bought = 0
    __money_earned = 0
    def set_money(self, money):
        self.__money += money

    def set_food(self, food):
        self.__food += food

    def set_cat_food(self, cat_food):
        self.__cat_food += cat_food

    def set_dirt(self, dirt):
        self.__dirt += dirt
    def food_eaten(self, food):
        self.__food_eaten += food

    def coats_bought(self):
        self.__coats_bought += 1
    def money_earned(self, money):
        self.__money_earned += money
    def get_money(self):
        return self.__money

    def get_food(self):
        return self.__food

    def get_cat_food(self):
        return self.__cat_food

    def get_dirt(self):
        return self.__dirt
    def get_food_eaten(self):
        return self.__food_eaten
    def get_coats_bought(self):
        return self.__coats_bought
    def get_money_earned(self):
        return self.__money_earned

class Lodger:
    __hungry = 30
    __happy = 100
    __live = True
    def __init__(self, name, home):
        self.__name = name
        self.__home = home

    def pet(self):
        self.set_happy(5)
        print(f'{self.get_name()} гладит кота, счастье теперь = {self.get_happy()}')

    def eat(self):
        eat = 30
        if self.get_home().get_food <= eat:
            eat = self.get_home().get.food
            print(f'В холодильнике всего {self.get_home().get_food}')
        self.set_hungry(eat)
        self.get_home().set_food(-eat)
        self.get_home().food_eaten(eat)
        print(f'{self.get_name()} кушает, теперь сытость = {self.get_hungry()},'
              f' а еды в доме = {self.get_home().get_food}')
    def set_hungry(self, hungry):
        self.__hungry += hungry
    def set_happy(self, happy):
        self.__happy += happy
    def dead(self):
        self.__live += False

    def get_happy(self):
        return self.__happy
    def get_hungry(self):
        return self.__hungry
    def get_live(self):
        return self.__live
    def get_name(self):
        return self.__name
    def get_home(self):
        return self.__home

    def happy_down(self):
        self.set_happy(-10)
        print(f'Радость {self.get_name()} уменьшилась, теперь она = {self.get_happy()}')

class Husband(Lodger):
    def play(self):
        self.set_happy(20)
        self.happy_down()

    def work(self):
        self.happy_down()
        self.get_home().set_money(150)
        self.get_home().get_money_earned(150)
        print(f'{self.get_name()} поработал, теперь денег в доме {self.get_home().get_money()}')

class Wife(Lodger):

    def buy_food(self):
        self.happy_down()
        food = 100
        if self.get_home().get_money() < food:
            food = self.get_home().get_money()
            print(f'денег в доме всего на {self.get_home().get_money()} еды')
        self.get_home().set_food(food)
        self.get_home().set_money(-food)
        print(f'{self.get_name()} покупает {food} еды!')
    def buy_coat(self):
        if self.get_home().get_money() >= 350:
            self.get_home().set_money(-350)
            self.set_happy(60)
            self.get_home().get_coats_bought()
            print(f'{self.get_name()} покупает ШУБУ!, теперь ее счастье несоизмеримо и равно {self.get_happy()}'
                  f'\nА денег в доме остается {self.get_home().get_money()}')

    def clean_up(self):
        self.happy_down()
        anti_dirt = 100
        if self.get_home().get_dirt() < anti_dirt:
            anti_dirt = self.get_home().get_dirt()
        self.get_home().set_dirt(-anti_dirt)
        print(f'{self.get_name()} убралась, теперь в доме {self.get_home().get_dirt()} грязи')

class Cat(Lodger):
    def eat(self):
        eat = 10
        if self.get_home().get_cat_food <= eat:
            eat = self.get_home().get_cat_food
            print(f'Еды у кота всего {self.get_home().get_cat_food}')
        self.set_hungry(eat)
        self.get_home().set_cat_food(-eat)
        print(f'КОТ кушает, теперь сытость = {self.get_hungry()},'
              f' а кошачьей еды в доме = {self.get_home().get_cat_food}')

    def sleep(self):
        self.happy_down()
        print('Кот решает поспать!')

    def destroing(self):
        self.happy_down()
        self.get_home().set_dirt(5)
        print(f'Кот дерет обои! Уровень грязи в доме вырастает до {self.get_home().get_dirt()}')