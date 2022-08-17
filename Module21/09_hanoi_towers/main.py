def move(count_discs, x, y):
    def z(x, y):
        return ({1, 2, 3} - {x} - {y}).pop()

    if count_discs:
        z = z(x, y)
        move(count_discs - 1, x, z)
        print('Переложить диск {disc} со стержня номер {x} на стержень номер {y}'.format(
            disc=count_discs,
            x=x,
            y=y
        ))
        move(count_discs - 1, z, y)


count_discs = int(input('Введите количество дисков: '))
move(count_discs, 1, 3)
