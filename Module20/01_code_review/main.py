students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
# иногда, проще снести все и построить заново

surname = sum([len(students[id]['surname']) for id, deep in students.items()])
interests = [elem for _, deep in students.items() for elem in deep['interests']]
id_age = list(zip([aidi for aidi, inside in students.items()],
                  [inside['age'] for aidi, inside in students.items()]))

print('Список пар "ID студента — возраст": ', id_age)
print('Полный список интересов всех студентов', interests)
print('Общая длина всех фамилий студентов:', surname)

# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)
