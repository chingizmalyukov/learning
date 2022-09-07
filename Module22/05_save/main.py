import os

text = input('Введите строку: ')

print('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел): ')
splited_path = input()

file_name = input('\nВведите имя файла: ')
path = ''

for i_elem in splited_path.split():
    path = os.path.join(path, i_elem)
if os.path.exists(path):
    path = os.path.join(path, file_name)
    if os.path.exists(path):
        answer = input('Вы действительно хотите перезаписать файл?(Y/N): ').islower()
        if answer == 'y':
            file = open(path, 'w')
            file.write(text)
            file.close()
            print('Файл успешно перезаписан!')
        else:
            print('Изменения НЕ сохранены!')
    else:
        file = open(path, 'w')
        file.write(text)
        file.close()
        print('Файл успешно сохранён!')
