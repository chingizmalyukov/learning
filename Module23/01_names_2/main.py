def solution(file_name):
    solution_summ = 0
    string_number = 0
    with open(file_name, 'r', encoding='utf-8') as file, \
            open('errors.txt', 'w', encoding='utf-8') as errors_log:
        for i_name in file:
            string_number += 1
            if i_name.endswith('\n'):
                name = i_name[:-1]
            else:
                name = i_name
            try:
                if len(name) < 3:
                    raise ZeroDivisionError
            except ZeroDivisionError:
                print(f'Ошибка: менее трёх символов в строке {string_number}')
                errors_log.write(str(f'Ошибка! В троке {string_number} менее 3 символов!\n'))
            else:
                solution_summ += len(name)
    return solution_summ


file_name = 'people.txt'
print(solution(file_name))
