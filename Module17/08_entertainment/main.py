# я не знаю какой сумасшедший формулировал текст задачи, но воспринимать
#его физически больно.
import random

stick_count = int(input("Kоличество палок: "))
stick_up = ['I' for _ in range(stick_count)]
num_stones = int(input("Количество бросков: "))


for throw in range(num_stones):
    print('Бросок', throw + 1, end = '. ')
    start = random.randint(1, stick_count)
    print('Сбиты палки с номера', start)
    finish = random.randint(start, stick_count)
    print('по номер ', finish)


    for stick in range(start, finish + 1):
        stick_up[stick - 1] = '.'

print('\nРезультат:', ''.join(stick_up))