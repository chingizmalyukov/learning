class Property:
    __devisor = 0

    def __init__(self, worth):
        self.set_worth(worth)

    def get_worth(self):
        return self.__worth

    def get_divisor(self):
        return self.__devisor

    def set_worth(self, worth):
        self.__worth = worth

    def set_divisor(self, devisor):
        self.__devisor = devisor

    def math(self):
        tax = int(self.get_worth()) * (1 / self.get_divisor())
        return tax


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.set_divisor(1000)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.set_divisor(200)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.set_divisor(500)


numbers = [1, 2, 3]
property_dict = {1: 'квартиры', 2: 'машины', 3: 'дачи'}
summ_taxes = 0
print('Добро пожаловать в приложение для подсчета налога.\nПросто следуйте инструкциям на экране.')
while True:

    print('\nУкажите имеющееся имущество:\n 1 - Квартира, 2 - Машина, 3 - Дача')
    while True:
        answer = int(input())
        if answer in numbers:
            break
        else:
            print('Некорректный ввод!\n 1 - Квартира, 2 - Машина, 3 - Дача')

    while True:
        worth = input(f'Укажите стоимость {property_dict[answer]}: ')
        if worth.isdigit():
            break
        else:
            print('Стоимость нужно указать в цифрах!\n')

    if answer == 1:
        property = Apartment(worth)
    elif answer == 2:
        property = Car(worth)
    else:
        property = CountryHouse(worth)

    summ_taxes += round(property.math(), 2)
    print(f'налог с {property_dict[answer]} = {property.math()}\nобщая сумма налогов = {summ_taxes}')

    quest = input('Добавить еще имущество?(да\нет): ')
    if not quest.lower() == 'да':
        break

money = int(input('\nУкажите кол-во имеющихся денежных средств: '))
if money > summ_taxes:
    print(f'Ура! Вам хватает на уплату налогов, и даже останется {money - summ_taxes}!')
elif money < summ_taxes:
    print(f'Так, вам не хватает для уплаты налогов всего {summ_taxes - money}!')
else:
    print('У вас есть ровно столько, сколько нужно для уплаты налогов!')
