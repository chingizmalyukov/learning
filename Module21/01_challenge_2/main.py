def printer(num, count=1):
    print(count)
    if count != num:
        printer(num, count + 1)


num = int(input('Введите num: '))
printer(num)