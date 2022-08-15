def check (tuple_sount)
    flag = True
    for num in tuple_sount:
        if num % round(num, 0) != 0:
            print(tuple_sount)
            flag = False
            break
    if flag:
        print(tuple(sorted(tuple_sount)))

# tuple_sount = (5, 2, -4, 6, 2, 1)
# check(tuple_sount)
# TODO код раскомментировать, исправить опечатку - так как он выдаёт синтаксическую ошибку