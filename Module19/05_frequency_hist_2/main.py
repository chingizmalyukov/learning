letter_dict = dict()
string = input('Введите текст: ')

for letter in string:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1

for

print(letter_dict)