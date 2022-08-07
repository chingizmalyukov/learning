first_clas = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
sorted_class = []

first_clas.extend(second_class)

for _ in range(len(first_clas)):
    smaller_man = first_clas[0]
    for man in first_clas:
        if man < smaller_man:
            smaller_man = man

    count = first_clas.count(man)

    for _ in range(count):
        sorted_class.append(smaller_man)
        first_clas.remove(smaller_man)

print('Отсортированный список учеников:', sorted_class)
