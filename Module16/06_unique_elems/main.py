first_list = []
second_list = []

for i in range (3):
    print('Введите', i+1, '-е число для первого списка:', end=' ')
    num = int(input())
    first_list.append(num)

for i in range (7):
    print('Введите', i+1, '-е число для второго списка:', end=' ')
    num = int(input())
    second_list.append(num)


print('\nПервый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)
sorted_list = list(set(first_list))

print('\nНовый первый список с уникальными элементами:', sorted_list)