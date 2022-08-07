a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
first_num = a.count(5)
for _ in range(first_num):
    a.remove(5)
a.extend(c)
second_num = a.count(3)

print('Результат работы программы:')
print('Кол-во цифр 5 при первом объединениее:', first_num)
print('Кол-во цифр 3 при втором объединениее:', second_num)
print('Итоговый список:', a)
