# class Example_1:
#     def __add__(self, other):
#         return Example_2()
#
# class Example_2:
#     answer = 'сложили два класса и вывели'
#
# a = Example_1()
# b = Example_2()
# c = a + b
# print(c.answer)
# ЭТО ВЫ ВОТ ТАК ОБЪЯСНИЛИ ЦЕЛЫЙ МЕТОД __add__ О КОТОРОМ ДО ЭТОГО ВООБЩЕ НИСЛОВА НЕ БЫЛО??
# В ОЧЕРЕДНОЙ РАЗ ПРИШЛОСЬ ГУГЛИТЬ ТЕОРИЮ

class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return Another()


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return Another()


class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return Another()


class Earth:
    def __add__(self, other):
        if isinstance(other, Dust):
            return Lightning()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return Another()


class Storm:
    answer = 'Storm'


class Steam:
    answer = 'Steam'


class Dirt:
    answer = 'Dirt'


class Lightning:
    answer = 'Lightning'


class Dust:
    answer = 'Dust'


class Lava:
    answer = 'Lava'


class Another:
    answer = 'None'


a = Water()
b = Water()
c = a + b

print(c.answer)
