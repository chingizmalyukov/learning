text = input('Введите строку: ')
bigger_word = max(text.split(), key=len)
print('Самое длинное слов:', max(text.split(), key=len))
print('Длина этого слова:', len(bigger_word))