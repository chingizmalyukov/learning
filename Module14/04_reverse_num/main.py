def action(num):
    reversed_num = 0
    while num != 0:
        reversed_num *= 10
        reversed_num += num % 10
        num //= 10
    return reversed_num
def reversing(num):
    flag = True
    fraction_count = 0
    whole = ''
    fraction = ''
    for sym in num:
        if sym == '.':
            flag = False
        elif flag:
            whole = whole + sym
        else:
            fraction = fraction + sym
            fraction_count += 1
    num_reversed = action(float(whole)) + (action(float(fraction)) * 10 ** -fraction_count)
    return num_reversed

n = input('Введите первое число: ')
k = input('Введите второе число: ')
print()
print('Первое число наоборот:', reversing(n))
print('Второе число наоборот:', reversing(k))
print('Сумма:', reversing(n) + reversing(k))