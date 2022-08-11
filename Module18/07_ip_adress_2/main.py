def ip_check(string):
    flag = True
    if len(string) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
    for symbol in string:
        if not symbol.isdigit():
            print(symbol, '— это не целое число.')
            flag = False
            break
        elif int(symbol) > 255:
            print(symbol, 'превышает 255.')
            flag = False
            break
        elif int(symbol) < 0:
            print(symbol, 'меньше 0')
            flag = False
            break
    return flag

string = input('Введите IP: ').split('.')

if ip_check(string):
    print('IP-адрес корректен')