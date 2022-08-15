def comparison(surname, word):
    flag = False
    bigger_word = surname[:-1]
    if len(word) != len(surname):
        if len(word) > len(surname):
            if surname == word[:-1]:
                flag = True
        else:
            if bigger_word == word:
                flag = True
    else:
        flag = True
    return flag

database = {  # TODO в коде не хватает пары пустых строк по PEP8
    ('Татьяна', 'Иванова'): 23,
    ('Иван', 'Иванов'): 21,
}

surname = input('Введите фамилию: ').lower()

for key, age in database.items():
    word = key[1].lower()
    if comparison(surname, word):
        print(key[0], key[1], age)