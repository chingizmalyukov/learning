database = {1: [0, 'anon'],
            2: [0, 'anon'],
            3: [0, 'anon']
            }

count = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
step = 3

for i in range(1, count + 1):
    result = input(f'{i}-я запись: ').split()
    for key, dat in database.items():
        if int(dat[0]) < int(result[0]):
            if key == 1:
                database[3][0] = database[2][0]
                database[3][1] = database[2][1]
                database[2][0] = database[1][0]
                database[2][1] = database[1][1]
                dat[0] = result[0]
                dat[1] = result[1]
            elif key == 2:
                database[3][0] = database[2][0]
                database[3][1] = database[2][1]
                dat[0] = result[0]
                dat[1] = result[1]
            elif key == 3:
                dat[0] = result[0]
                dat[1] = result[1]
            break

print('Итоги соревнований:')
for i, info in database.items():
    print(f'{i}-е место. {info[1]} ({info[0]})')
