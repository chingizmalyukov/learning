import random

original_list = [random.randint(0, 10) for _ in range(10)]
new_list = [tuple([original_list[i], original_list[i + 1]]) for i in range(0, 10, 2)]

print('Оригинальный список:', original_list)
print('Новый список:', new_list)