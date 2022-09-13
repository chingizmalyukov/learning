def check(i_string):
    flag = True
    try:
        if len(i_string.split()) != 3:
            raise IndexError
        elif not i_string.split()[0].isalpha():
            raise NameError
        elif '.' not in list(i_string.split()[1]) or '@' not in list(i_string.split()[1]):
            raise SyntaxError
        elif int(i_string.split()[2]) > 99 or int(i_string.split()[2]) < 10:
            raise ValueError

    except IndexError:
        print(f'{i_string},   НЕ присутствуют все три поля')
    except NameError:
        print(f'{i_string},   Поле «Имя» содержит НЕ только буквы')
    except SyntaxError:
        print(f'{i_string},   Поле «Имейл» НЕ содержит @ и . (точку)')
    except ValueError:
        print(f'{i_string},   Поле «Возраст» НЕ является числом от 10 до 99')
    else:
        good.write(i_string)
        good.write('\n')
        flag = False
    return flag


def printer(file_name):
    print(f'\nСодержимое файла {file_name}:')
    log = open(file_name, 'r', encoding='utf-8')
    for i_log in log:
        print(i_log, end='')
    log.close()


file = open('registrations.txt', 'r', encoding='utf-8')
good = open('registrations_good.log', 'w', encoding='utf-8')
bad = open('registrations_bad.log', 'w', encoding='utf-8')

for i_string in file:
    if i_string.endswith('\n'):
        if check(i_string[:-1]):
            bad.write(i_string)
    else:
        if check(i_string):
            bad.write(i_string)

file.close()
good.close()
bad.close()

printer('registrations.txt')
printer('registrations.txt')
