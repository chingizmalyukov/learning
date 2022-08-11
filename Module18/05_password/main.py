def check(password):
    dig_count = 0
    flag = False
    for i_letter in password:
        if i_letter.isupper():
            flag = True
            break
    if flag:
        if len(password) < 8:
            flag = False
            return flag
        else:
            for letter in password:
                if letter.isdigit():
                    dig_count += 1
            if dig_count < 3:
                flag = False
                return flag
    else:
        return flag
    return flag

while True:
    password = input('Введите пароль: ')
    if check(password) == True:
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')