shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input('Название детали: ')
count = 0
price = 0
for item in shop:
    if item[0] == name:
        price += item[1]
        count += 1

print('Кол-во деталей:', count)
print('Общая стоимость:', price)
