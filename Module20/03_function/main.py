def painting(string, num):
    if string.count(num) > 1:
        first_place = string.index(num)
        new_seq = string[first_place + 1:]
        second_place_2 = new_seq.index(num)
        solution_seq = string[first_place:first_place + second_place_2 + 2]
        print(solution_seq)
    elif string.count(num) == 1:
        print(string[string.index(num):])
    else:
        print('пустой кортеж')

# TODO в коде нужно реализовать пример использования данного функционала
