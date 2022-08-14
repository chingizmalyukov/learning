number_dick = {1: 'Первая', 2: 'Вторая', 3: 'Третья', 4: 'Четвертая',
                5: 'Пятая', 6: 'Шестая', 7: 'Седьмая', 8: 'Восьмая', 9: 'Девятая'}
text_dict = dict()
count = int(input('Введите количество пар слов: '))

for i_count in range(1, count + 1):
    text = input(f'{number_dick[i_count]} пара: ').lower().split(' - ')
    text_dict[text[0]] = text[1]
    text_dict[text[1]] = text[0]


while True:
    word = input('\nВведите слово: ').lower()
    if word in text_dict:
        print('Синоним:', text_dict[word])
    else:
        print('Такого слова в словаре нет.')