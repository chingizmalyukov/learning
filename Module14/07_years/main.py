def comparison (num, step):
    flag = False
    dig = num // 10 ** step % 10
    cons = 0
    while num != 0:
        if num % 10 == dig:
            cons += 1
        num //= 10
    if cons >= 3:
        flag = True
    else:
        step += 1
    return flag

step = 0
start = int(input('Введите первый год: '))
finish = int(input('Введите второй год: '))
print()
print('Годы от',start, 'до', finish, 'с тремя одинаковыми цифрами:')
for num in range (start, finish + 1):
    flag = comparison(num, step)
    if flag:
        print(num)