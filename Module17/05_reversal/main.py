text = input('Введите строку: ')
x = 0
start = text.index('h')
fin = len(text) - (text[::-1].index('h') + 1)
print('Развёрнутая последовательность между первым и последним h:',
       text[fin - 1 : start : -1])
