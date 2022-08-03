def min_div_found(num):
    if num < 1:
        print('Ошибка ввода. Число должно быть больше 1. ')
    elif num % 2 == 0:
        min_div = 2
    else:
        for div in range(2, num + 1):
            if num % div == 0:
                min_div = div
                break
    print('Наименьший делитель, отличный от единицы:', min_div)


n = int(input('Введите число: '))
min_div_found(n)
