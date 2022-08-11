def solution(first_string, second_string):
    flag = False
    count = 0
    if first_string == second_string:
        count = 0
        flag = True
    elif len(first_string) == len(second_string):
        for i in range(len(first_string)):
            first_string = first_string[-1:] + first_string[:-1]
            if first_string == second_string:
                count = i + 1
                flag = True
    return flag, count


first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')
flag, count = solution(first_string, second_string)

if flag:
    print('\nПервая строка получается из второй со сдвигом', count)
else:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
