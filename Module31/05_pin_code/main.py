import itertools

solution = len(list(itertools.combinations_with_replacement('0123456789', 4)))
print(solution)  # TODO Всего вариантов должно быть 10 000 (математика: 10*10*10*10)
#  сейчас выдаёт не всё, которые ожидаем потому, что здесь нужен другой метод или подход

# for i_password in solution:
#     print(i_password)
