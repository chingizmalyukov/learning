import random


class Carma:
    need_carma = 500
    __carma = 0
    __day = 1

    errors_list = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']

    def one_day(self):
        number = random.randint(1, 10)
        if number == 1:
            self.errors()
        else:
            number = random.randint(1, 7)
            self.set_carma(number)
        self.set_day()
        return self.carma_check()

    def set_carma(self, number):
        self.__carma += number

    def set_day(self):
        self.__day += 1

    def get_carma(self):
        return self.__carma

    def get_day(self):
        return self.__day

    def errors(self):
        error = f'{self.get_day()} день, {random.choice(self.errors_list)}\n'
        file = open('error.txt', 'a')
        file.write(error)
        file.close()

    def carma_check(self):
        if self.get_carma() >= self.need_carma:
            return True
        else:
            return False


carma_1 = Carma()

while True:
    if carma_1.one_day():
        break

print(f'Кол-во дней до просветления = {carma_1.get_day()}')
