consonants = ['а', 'е', 'и', 'о', 'у', 'ы', 'э']

text = input('Введите текст: ')

letters_in_text = [letter for letter in text if letter in consonants]

print('\nСписок гласных букв:', letters_in_text)
print('длина списка:', len(letters_in_text))
