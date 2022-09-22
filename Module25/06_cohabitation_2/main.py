import random


class Home:
    __days_lived = 0
    __money = 100
    __food = 50
    __cat_food = 30
    __dirt = 0
    __food_eaten = 0
    __coats_bought = 0
    __money_earned = 0
    __need_cat_food = False

    def days_lived_up(self):
        self.__days_lived += 1

    def set_money(self, money):
        self.__money += money

    def set_food(self, food):
        self.__food += food

    def set_cat_food(self, cat_food):
        self.__cat_food += cat_food

    def set_dirt(self, dirt):
        self.__dirt += dirt

    def set_need_cat_food(self):
        if self.get_need_cat_food():
            self.__need_cat_food = False
            print('Закупили еды для кота!')
        else:
            self.__need_cat_food = True
            print('У пушистого кончилась еда!')

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

    def get_days_lived(self):
        return self.__days_lived

    def get_need_cat_food(self):
        return self.__need_cat_food


class Lodger:
    __hungry = 30
    __happy = 100
    __live = False

    def __init__(self, name, home):
        self.__name = name
        self.__home = home

    def set_hungry(self, hungry):
        self.__hungry += hungry

    def set_happy(self, happy):
        self.__happy += happy

    def dead(self):
        self.__live = True

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

    def hangry_down(self):
        self.set_hungry(-10)
        print(f'Сытость {self.get_name()} уменьшилась, теперь она = {self.get_hungry()}')

    def happy_up(self):
        pass

    def food_up(self):
        pass

    def pet(self):
        self.set_happy(5)
        print(f'{self.get_name()} гладит кота, счастье теперь = {self.get_happy()}')

    def eat(self):
        if self.get_home().get_food <= 0:
            self.food_up()
        else:
            eat = 30
            if self.get_home().get_food() <= eat:  # NOTE пример исправления ошибки. Далее - аналогичным образом
                eat = self.get_home().get.food  # TODO опечатка: get.food -> get_food (+скобки, см. комментарий ниже)
                print(f'В холодильнике всего {self.get_home().get_food}')
            self.set_hungry(eat)
            self.get_home().set_food(-eat)
            self.get_home().food_eaten(eat)
            print(f'{self.get_name()} кушает, теперь сытость = {self.get_hungry()},'
                  f' а еды в доме = {self.get_home().get_food}')

    def day(self):
        self.get_home().days_lived_up()
        print(f'\nДень {self.get_home().get_days_lived()}')
        if self.get_hungry() <= self.get_happy() - 10:
            if self.get_hungry() <= 40:
                self.eat()
        else:
            if self.get_happy() <= 60:
                self.happy_up()
        if self.get_hungry() < 0:
            print(f'{self.get_name()} умирает от голода! Игра окончена =(')
            self.dead()
            return self.get_live()
        else:
            if self.get_happy() < 10:
                print(f'{self.get_name()} вскрывается из-за депрессии! Игра окончена =(')
                self.dead()
                return self.get_live()
            else:
                if self.get_home().get_dirt() > 90:
                    self.set_happy(-10)
                    print(f'Уровень грязи в доме {self.get_home().get_dirt()}, счастье утекает!')
                return self.get_live()


class Husband(Lodger):
    def happy_up(self):
        choise = random.randint(1, 2)
        if choise == 1:
            self.set_happy(20)
            self.hangry_down()
            print(f'Муж принимает ответственное решение поиграть в компьютер!(счастье теперь {self.get_happy()}')
        else:
            self.pet()

    def food_up(self):
        self.get_home().set_money(150)
        self.get_home().get_money_earned(150)
        self.hangry_down()
        print(f'{self.get_name()} поработал, теперь денег в доме {self.get_home().get_money()}')


class Wife(Lodger):

    def food_up(self):
        if self.get_home().get_money() == 0:
            self.clean_up()
        else:
            food = 100
            if self.get_home().get_money() < food:
                food = self.get_home().get_money()
                print(f'денег в доме всего на {self.get_home().get_money()} еды')
            self.get_home().set_food(food)
            self.get_home().set_money(-food)
            print(f'{self.get_name()} покупает {food} еды!')
            if self.get_home().get_need_cat_food():
                print('У кота закончилась еда, берем ему тоже!')
                cat_food = 30
                if self.get_home().get_money() < cat_food:
                    cat_food = self.get_home().get_money()
                    print(f'Денег мало, по этому купим всего {cat_food} еды для пушистого.')
                self.get_home().set_cat_food(cat_food)
                if cat_food != 0:
                    self.get_home().set_need_cat_food()
            self.hangry_down()

    def happy_up(self):
        if self.get_home().get_money() >= 350:
            self.get_home().set_money(-350)
            self.set_happy(60)
            self.get_home().get_coats_bought()
            self.hangry_down()
            print(f'{self.get_name()} покупает ШУБУ!, теперь ее счастье несоизмеримо и равно {self.get_happy()}'
                  f'\nА денег в доме остается {self.get_home().get_money()}')
        else:
            self.pet()
            print(f'Денег на шубу нет, пойду кота поглажу хоть.(уровень счастья = {self.get_happy()}')

    def clean_up(self):
        anti_dirt = 100
        if self.get_home().get_dirt() < anti_dirt:
            anti_dirt = self.get_home().get_dirt()
        self.get_home().set_dirt(-anti_dirt)
        self.hangry_down()
        print(f'{self.get_name()} убралась, теперь в доме {self.get_home().get_dirt()} грязи')


class Cat(Lodger):
    def eat(self):
        if self.get_home().get_cat_food == 0:
            self.sleep()
            self.get_home().set_need_cat_food()
        else:
            eat = 10
            if self.get_home().get_cat_food <= eat:
                eat = self.get_home().get_cat_food
                print(f'Еды у кота всего {self.get_home().get_cat_food}')
                self.get_home().set_need_cat_food()
            self.set_hungry(eat)
            self.get_home().set_cat_food(-eat)
            print(f'КОТ кушает, теперь его сытость = {self.get_hungry()},'
                  f' а кошачьей еды в доме = {self.get_home().get_cat_food}')

    def sleep(self):
        self.hangry_down()
        print('Кот решает поспать!')

    def happy_up(self):
        self.set_happy(30)
        self.get_home().set_dirt(5)
        print(f'Кот дерет обои! Уровень грязи в доме вырастает до {self.get_home().get_dirt()},'
              f'\n А уровень счастья кота до {self.get_happy()}')


home_1 = Home()
husband_1 = Husband('Муж', home_1)
wife_1 = Wife('Жена', home_1)
cat_1 = Cat('Кот', home_1)

for day in range(1, 366):
    if husband_1.day() or wife_1.day() or cat_1.day():
        break

print(f'Всего прожито дней: {home_1.get_days_lived()}'
      f'\nДенег заработано: {home_1.get_money_earned()}'
      f'\nЕды скушано: {home_1.get_food_eaten()}'
      f'\nШуб куплено: {home_1.get_coats_bought()}')

# возникает ошибка:
#   File "X:\GIT\python_basic\Module25\06_cohabitation_2\main.py", line 123, in eat
#     if self.get_home().get_food <= 0:
# TypeError: '<=' not supported between instances of 'method' and 'int'
# на сколько понимаю, это связано с тем, что передается метод, а не значение
# так и не понял как сделать, чтобы передовалось значение(

# NOTE эта ошибка исправляется просто: во всех попытках обратиться к методу получения значения количества еды,
#  нужно добавить круглые скобки. То есть, вместо self.get_home().get_food нужно записывать self.get_home().get_food()
#  первый вариант записи - это обращение к полю класса, но так как у нас есть метод-геттер, то вызываем его.
#  И логично, раз это метод, то ему присущи круглые скобки каждый раз, когда мы его вызываем.
# Как минимум ещё в одном месте в коде возникнет подобная ошибка: при попытках вызова метода get_cat_food
