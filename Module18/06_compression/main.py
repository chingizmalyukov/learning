string = input('Введите строку: ')
zipped_string = ''
letter_number = 0
count = 0

for i, symbol in enumerate(string):
    if symbol == string[letter_number]:
        count += 1
    else:
        zipped_string = (''.join([zipped_string, string[letter_number], str(count)]))
        letter_number = i
        count = 1
zipped_string = (''.join([zipped_string, string[letter_number], str(count)]))


print(zipped_string)