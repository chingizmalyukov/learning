list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break
def generator(list_1, list_2, to_find):
    # можно входные данные тоже записать в генератор, но так он потеряет универсальность
    # NOTE соглашусь. Пусть входные данные будут вне генератора, да и в контексте задачи они идеально качестве констант
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result == to_find:
                return print('Found!!!')


generator(list_1, list_2, to_find)
