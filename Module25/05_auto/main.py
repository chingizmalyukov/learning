import math


class Car:
    __angel = 90
    __x = 0
    __y = 0

    def move(self, dist):
        print(f'Врум-Врум Машина приехала из точки [{self.get_x()},{self.get_y()}]', end=' ')
        x = round(self.get_x() + dist * math.cos(self.get_angel()), 2)
        self.set_x(x)
        y = round(self.get_y() + dist * math.sin(self.get_angel()), 2)
        self.set_y(y)
        print(f'в точку [{self.get_x()},{self.get_y()}]\n')

    def change(self):
        print('Куда поворачиваем?')
        turn = int(input('0 - налево, 1 - направо: '))
        if turn == 0:
            word = 'налево'
            if self.get_angel() == 360:
                self.set_angel(0)
                self.change_angel(+90)
        else:
            word = 'направо'
            if self.get_angel() == 0:
                self.set_angel(360)
                self.change_angel(-90)
        print(f'Повернули {word}!\n')

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_angel(self, angel):
        self.__angel = angel

    def change_angel(self, turn):
        self.__angel += turn

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_angel(self):
        return self.__angel


class Bus(Car):
    __passengers = 0
    __max_passengers = 90
    __ticket = 1
    __money = 0

    def get_passengers(self):
        return self.__passengers

    def get_money(self):
        return self.__money

    def move(self, dist):
        print(f'ИНФО: Кол-во пассажиров = {self.get_passengers()}'
              f' | Кол-во заработанных денег = {self.get_money()}')
        print(f'Автобус выехал из точки [{self.get_x()},{self.get_y()}]')
        x = round(self.get_x() + dist * math.cos(self.get_angel()), 2)
        self.set_x(x)
        y = round(self.get_y() + dist * math.sin(self.get_angel()), 2)
        self.set_y(y)

        out_passenger = int(input('Кол-во вышедших пассажиров: '))
        self.__passengers -= out_passenger
        if self.__passengers < 0:
            self.__passengers = 0

        in_passenger = int(input('Кол-во вошедших пассажиров: '))
        free_places = self.__max_passengers - self.get_passengers()
        if free_places < in_passenger:
            print(f'Места кончаются, можем взять только {free_places}')
            in_passenger = free_places
        self.__money += in_passenger * self.__ticket
        self.__passengers += in_passenger
        print(f'Сумма оплаты за проезд = {in_passenger * self.__ticket}')
        print(f'Автобус в точке [{self.get_x()},{self.get_y()}]\n')


print('Cтартуем!')
while True:
    chose = int(input('Выберите транспортное средство(1 - машина, 2 - автобус, 3 выход): '))
    if chose == 1:
        transport = Car()
        print('вы выбрали АВТОМОБИЛЬ!\n')
    elif chose == 2:
        transport = Bus()
        print('вы выбрали АВТОБУС! \nАвтобус едет от остановки к остановке, каждый раз беря и высаживая пассажиров!\n')
    else:
        break
    while True:
        action = int(input('Выберите действие(1 - ехать, 2 - повернуть, 3 - выбрать другой транспорт): '))
        if action == 1:
            transport.move(1)
        elif action == 2:
            transport.change()
        else:
            break
