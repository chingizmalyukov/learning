number_dick = [{1: 'Первая', 2: 'Вторая', 3: 'Третья', 4: 'Четвертая',
                5: 'Пятая', 6: 'Шестая', 7: 'Седьмая', 8: 'Восьмая', 9: 'Девятая'},
               {1: 'Первый', 2: 'Второй', 3: 'Третий'}
               ]
country_city = dict()
country_count = int(input('Количество стран: '))

for i in range(1, country_count + 1):
    value = input(f'{number_dick[0][i]} страна: ').split()
    for town in value[1:]:
        country_city[town] = value[0]
print(country_city)

for i in range(1, 4):
    print(f'\n{number_dick[1][i]} город: ', end='')
    quest_city = input('')

    country = country_city.get(quest_city)
    if country:
        print(f'Город {quest_city} расположен в стране {country}.')
    else:
        print(f'По городу {quest_city} данных нет.')