import random
count = int(input('Количество чисел в списке: '))
list_nums = [random.randint(0,2) for _ in range(count)]
print('Список до сжатия: ', list_nums)

zipped_list = [number for number in list_nums if number != 0]
print('Список после сжатия:', zipped_list)