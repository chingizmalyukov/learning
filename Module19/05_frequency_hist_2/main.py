text = input('Введите текст: ')
text_dict = dict()
sym_dict = dict()
print('Оригинальный словарь частот: ')
for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

for i_sym in sorted(sym_dict.keys()):
    print(i_sym, ':', sym_dict[i_sym])

print('\nИнвертированный словарь частот:')
for i_letter, i_num in sym_dict.items():
    text_dict.setdefault(i_num, []).append(i_letter)
for i in text_dict:
    print(i, ':', text_dict[i])

