consonants = ['а', 'е', 'и', 'о', 'у', 'ы', 'э']
#все поправил, спасибо за подсказку, в обучении про эту функцию ничего не говорили.
text = input('Введите текст: ')

letters_in_text = [letter for letter in text.casefold() if letter in consonants]

print('\nСписок гласных букв:', letters_in_text)
print('длина списка:', len(letters_in_text))
