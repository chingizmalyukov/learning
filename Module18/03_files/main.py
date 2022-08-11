symbol_list = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
text = input('Название файла: ')
flag = True
for i_symbol in symbol_list:
    if text.startswith(i_symbol):
        print('\nОшибка: название начинается на один из специальных символов.')
        flag = False
        break
    elif not text.endswith('.txt') and not text.endswith('.docx'):
        print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx.')
        flag = False
        break
if flag:
    print('\nФайл назван верно.')
