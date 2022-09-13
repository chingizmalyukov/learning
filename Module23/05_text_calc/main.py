result = []

with open('calc.txt', 'r') as file:
    for line in file.readlines():
        try:
            if line.endswith('\n'):
                result.append(eval(line[1:-2]))
            else:
                result.append(eval(line[1:]))
        except:
            if input('Обнаружена ошибка:' + line[1:] + 'Хотите исправить? ').lower() == 'да':
                line = input('Введите исправленную строку: ')
                result.append(eval(line))

print(sum(result))
