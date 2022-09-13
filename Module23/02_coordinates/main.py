import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'r') as input, open('result.txt', 'w') as output:
    count = 1
    for line in input:
        function_num = 1
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            function_num += 1
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            output.write(str(my_list))
            output.write('\n')
        except ZeroDivisionError as er:
            print(f"Ошибка в {count} итерации: "
                  f"\nДелитель в {function_num} функции = 0, а на ноль делить нельзя!")
            output.write('error\n')
        count += 1

# Убрал лишние пары, поправил вывод, чтобы было понятно на какой иенно итерации
# происходит ошибка. Также в файл теперь записывается слово "error" в строку,
# в которой произошла данная ошибка.
