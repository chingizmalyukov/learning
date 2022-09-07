def check(letter):
    if letter in dict_letters:
        dict_letters[letter] += 1
    else:
        dict_letters[letter] = 1


dict_letters = dict()
symbols_count = 0

file = open('text.txt', 'r')
for i_elem in file:
    for symbol in list(i_elem.lower()):
        if symbol.isalpha():
            symbols_count += 1
            check(symbol)
file.close()

for key, value in dict_letters.items():
    dict_letters[key] = round(value / symbols_count, 3)

file = open('analysis.txt', 'a')
# прежде чем давать задания на СОРТИРОВКУ, неплохо было бы рассказать хоть что-то про данную функцию,
# кроме "ну есть функция sorted, она сортирует"
sorted_dict = dict((sorted(dict_letters.items(), key=lambda x: x[1], reverse=True)))

for key, value in sorted_dict.items():
    file.write(str(key))
    file.write(' ')
    file.write(str(value))
    file.write('\n')
file.close()
