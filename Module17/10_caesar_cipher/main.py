def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift)
                           % 33] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_str_start = input('Введите строку: ')
shift = int(input('Введите сдвиг: '))
input_str = [symbol for symbol in input_str_start if symbol != '.']

output_str = caesar_cipher(input_str, shift)

print('Зашифрованная строка:', output_str + input_str_start[len(input_str_start) -1])

