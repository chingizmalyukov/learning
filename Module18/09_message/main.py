string = input('Сообщение: ')
solved_string = ''
start = 0

for i in range(len(string)):
    if string[i].isalpha() == False:
        new_word = string[start:i]
        solved_string += new_word[::-1] + string[i]
        start = i + 1
    elif string[i].isalpha() == True and i == len(string) - 1:
        new_word = string[start:i]
        solved_string += new_word[::-1]

print('Новое сообщение:', solved_string)
