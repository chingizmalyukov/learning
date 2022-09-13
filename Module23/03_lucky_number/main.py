import random


def fortune(flag):
    number = random.randint(0, 13)
    if number == 1:
        flag = False
    return flag


flag = True
summ = 0

with open('outfile.txt', 'w') as output:
    try:
        while True:
            number = int(input('Введите число: '))
            if not fortune(flag):
                raise FutureWarning
            output.write(str(number))
            output.write('\n')
            summ += number
            if summ >= 777:
                raise ZeroDivisionError

    except ZeroDivisionError:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    except FutureWarning:
        print('Вас постигла неудача!')

print('Содержимое файла out_file.txt:')
output = open('outfile.txt', 'r')
for i_num in output:
    print(i_num, end='')
output.close()
