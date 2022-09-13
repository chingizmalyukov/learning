def logoutput(file):
    try:
        log = open(file, 'r', encoding='utf-8')
        for line in log:
            print(line)
        log.close()
    except FileNotFoundError:
        print('Лога чата нет. Введите первое сообщение!\n')


def loginput(file, name, message):
    log = open(file, 'a')
    logged_message = name + ' ' + message + '\n'
    log.write(str(logged_message))
    log.close()


chat_log = dict()
name = input('ВВедите логин: ') + ':'

try:
    while True:
        print('Выберите одно из действий: \n 1 - Посмотреть текущий текст чата.'
              ' \n 2 - Отправить сообщение (затем вводит сообщение).'
              ' \n любое другое значение - разлогиниться.')
        answer = input('')
        if answer == '1':
            logoutput('log.txt')
        elif answer == '2':
            print('Введите сообщение: ')
            print(name, end=' ')
            message = input('')
            loginput('log.txt', name, message)
        else:
            raise ZeroDivisionError
except ZeroDivisionError:
    print(f'{name}, покинул чат!')

# Почему-то при использовании кириллицы, и выводе лога чата,
# программа выдает ошибку, что-то там про инкодинг,
# хотя я указал его в функции вывода лога.
# С латиницей таких проблем нет.
