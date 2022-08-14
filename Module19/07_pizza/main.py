number_dick = {1: 'Первая', 2: 'Вторая', 3: 'Третья', 4: 'Четвертая',
                5: 'Пятая', 6: 'Шестая', 7: 'Седьмая', 8: 'Восьмая', 9: 'Девятая'}
count = int(input('Введите кол-во заказов: '))
database = {}
for i in range(1, count + 1):
    order = input(f'{number_dick[i]} заказ: ')
    fio, pizza, amount = order.rsplit(maxsplit=3)
    amount = int(amount)
    if fio not in database:
        database[fio] = {pizza: amount}
    else:
        if pizza not in database[fio]:
            database[fio] |= {pizza: amount}
        else:
            database[fio][pizza] += amount
for fio, order in sorted(database.items()):
    print(f'{fio}:')
    for pizza, amount in sorted(order.items()):
        print('    ', pizza, amount)