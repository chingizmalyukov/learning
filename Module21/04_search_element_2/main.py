def find_key(struct, key, depth):
    if key in struct:
        return struct[key]
    if depth > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Введите искомый ключ: ')
quest = input('Хотите ввести максимальную глубину? Y/N: ').islower()
if quest == 'y':
    deep = int(input('Введите максимальную глубину: '))
else:
    deep = 10

print(find_key(site, user_key, deep))
