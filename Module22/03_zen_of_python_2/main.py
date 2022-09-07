def dict_forming(char):
    if char in letters_dict:
        letters_dict[char] += 1
    else:
        letters_dict[char] = 1


letters_dict = dict()
letters_count = 0
words_count = 0
string_count = 0
symbols = ['.', ',', '-', ' ', '!']

file = open('zen.txt', 'r')
for i_elem in file:
    for j_elem in i_elem.split():
        words_count += 1
    string_count += 1
    for char in list(i_elem.lower()):
        if char not in symbols:
            dict_forming(char)
file.close()

print(f'Количество букв в файле: {sum(letters_dict.values())} '
      f'\nКоличество слов в файле: {words_count}'
      f'\nКоличество строк в файле: {string_count}'
      f'\nНаиболее редкая буква: {min(letters_dict, key=letters_dict.get)}')
