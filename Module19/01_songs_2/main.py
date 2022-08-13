violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
number_dick = {
    1: 'первой',
    2: 'второй',
    3: 'третьей',
    4: 'четвертой',
    5: 'пятой',
    6: 'шестой',
    7: 'седьмой',
    8: 'восьмой',
    9: 'девятой'
}

full_time = 0
count = int(input('Сколько песен выбрать? '))
for i in range(count):
    name = input(f'Название {number_dick[i + 1]} песни: ')
    if name in violator_songs:
        full_time += violator_songs[name]

print(f'\nОбщее время звучания песен: {round(full_time, 2)} минуты')
