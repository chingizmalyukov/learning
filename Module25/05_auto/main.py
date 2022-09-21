import math


class Car:
    __angel = 90
    __x = 0
    __y = 0

    def move(self, dist):
        x = self.get_x() + dist * math.cos(self.get_angel())
        self.set_x(x)
        y = self.get_y() + dist * math.sin(self.get_angel())
        self.set_y(y)

    def change(self, turn):
        if turn == 0:
            if self.get_angel() == 360:
                self.set_angel(0)
                self.change_angel(+90)
        elif turn == 1:
            if self.get_angel() == 0:
                self.set_angel(360)
                self.change_angel(-90)

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

    def move(self, dist):
        x = self.get_x() + dist * math.cos(self.get_angel())
        self.set_x(x)
        y = self.get_y() + dist * math.sin(self.get_angel())
        self.set_y(y)

        out_passenger = int(input('Кол-во вышедших пассажиров:'))
        self.__passengers -= out_passenger
        if self.__passengers < 0:
            self.__passengers = 0

        in_passenger = int(input('Кол-во вошедших пассажиров: '))
        free_places = self.__max_passengers - self.get_passengers()
        if free_places < in_passenger:
            print(f'Места кончаются, можем взять только {free_places}')
            self.__money += free_places * self.__ticket
            self.__passengers += free_places
        else:
            self.__money += in_passenger * self.__ticket
            self.__passengers += in_passenger

# поворот влево - 0, вправо - 1. не стал заморачиваться, сделал поворот на 90 градусов за раз.
