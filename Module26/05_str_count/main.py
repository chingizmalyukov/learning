import os


def string_count(file_path):
    summ_strings = 0
    empty_symbols = ['', ' ', '\n', '', '\t']
    with open(file_path, 'r', encoding='utf-8') as file:
        for i_string in file:
            string = 0
            for i_symbol in i_string:
                if i_symbol not in empty_symbols:
                    string = 1
                    break
            summ_strings += string
        print(f'Кол-во строк кода в файле {file_path} = {summ_strings}')
        return summ_strings


def file_check(start_path):
    for i_item in os.listdir(start_path):
        file_path = os.path.join(start_path, i_item)
        # Хотел сделать дополнительно к заданию, чтобы функция проверяла файлы не только в указанной директории,
        # но и в директориях внутри. Попытался использовать знания о рекурсии,
        # но почему-то второй раз генератор внутри генератора не запускается
        # if os.path.isdir(file_path):
        #     file_check(file_path)
        # else:
        #     if file_path[len(file_path) - 3:] == '.py':
        #         yield file_path
        # NOTE Здесь если функцию делать рекурсивной (для обхода вложенных директорий),
        #  то в первый yield нужно передавать наименование директории, а во второй - количество строк.
        if file_path[len(file_path) - 3:] == '.py':
            yield file_path


start_path = input('Укажите директорию: ')

solution = 0

for file_path in file_check(start_path):
    solution += string_count(file_path)

print(f'Общее кол-во строк кода = {solution}')
