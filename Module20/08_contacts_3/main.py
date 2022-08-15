database = {}

while True:
    print('Введите номер действия: \n1. Добавить контакт \n2. Найти человека')
    action = int(input())
    if action == 1:
        key = input('Введите имя и фамилию нового контакта (через пробел): ').lower().title().split()
        if tuple(key) in database:
            print('Такой человек уже есть в контактах.')
        else:
            number = int(input('Введите номер телефона: '))
            database[tuple(key)] = number
        print('Текущий словарь контактов:', database)
    elif action == 2:
        surname = input('Введите фамилию для поиска: ').lower().title()
        for key, number in database.items():
            if surname in key:
                print(key[0], key[1], number)
                break
    else:
        print('Ошибка ввода! Необходимо ввести цифру 1 или 2')
