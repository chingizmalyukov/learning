guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    flag = False
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    answer = input('Гость пришел или ушел? ')
    if answer == 'Пора спать':
        print()
        break
    name = input('Имя гостя: ')
    if answer == 'ушел':
        for i_name in guests:
            if name == i_name:
                flag = True
        if flag:
            guests.remove(name)
            print('Пока,', name)
        else:
            print('Нет таких!')
    elif answer == 'пришел':
        if len(guests) >= 6:
            print('Прости,', name, ', но мест нет.')
        else:
            guests.append(name)
            print('Привет,', name, '!')
    print()
print('Вечеринка закончилась, все легли спать.')
