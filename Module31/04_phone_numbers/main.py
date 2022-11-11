import re

words_dict = {0: 'первый', 1: 'второй', 2: 'третий', 3: 'четвертый', 4: 'пятый'}
numbers = ['9999999999', '999999-999', '99999x9999']

patern = r'\b[89]\d{9}'

for count, i_num in enumerate(numbers):
    if re.fullmatch(patern, i_num):
        print(f'{words_dict[count]} номер: всё в порядке')
    else:
        print(f'{words_dict[count]} номер: не подходит')
