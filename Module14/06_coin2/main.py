def check(x, y, r):
    if (x ** 2 + y ** 2) ** 0.5 <= r: #можно было подключить math. и использовать sqrt
        print("Монетка где-то рядом") #но зачем это делать, когда можно не делать =)
    else:
        print('Монетки в области нет')

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
print()
check(x, y, r)
