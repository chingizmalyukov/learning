consonants = ['а', 'е', 'и', 'о', 'у', 'ы', 'э']
# TODO по условию задания нужно не только вывести в консоль сам список, но и его длину
#  кроме того, нужно воспользоваться методами для нивелирования регистра букв.
#  Что будет, если одна из гласных окажется заглавной? Например, как в предложении "Оно было яркое".
text = input('Введите текст: ')

letters_in_text = [letter for letter in text if letter in consonants]
# TODO в решении не учтены заглавные гласные буквы.
#  обратите внимание на метод .casefold()

print('\nСписок гласных букв:', letters_in_text)
print('длина списка:', len(letters_in_text))
