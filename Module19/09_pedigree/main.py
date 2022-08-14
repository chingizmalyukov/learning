def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])

number_dick = {1: 'Первая', 2: 'Вторая', 3: 'Третья', 4: 'Четвертая',
                5: 'Пятая', 6: 'Шестая', 7: 'Седьмая', 8: 'Восьмая', 9: 'Девятая'}

p_tree = {}
n = int(input('Введите количество человек: '))
for i in range(n - 1):
    child, parent = input(f'{number_dick[i+1]} пара: ').split()
    p_tree[child] = parent

heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)

for key, value in sorted(heights.items()):
    print(key, value)