import random


class Student:
    def __init__(self, name, number, grades):
        self.name = name
        self.number = number
        self.grades = grades

    def infoprint(self):
        print(self.name, self.number, self.grades)

    def summ(self):
        summ = sum(self.grades)
        return summ


student_1 = Student('первый', 47, [random.randint(1, 5) for _ in range(5)])
student_2 = Student('второй', 47, [random.randint(1, 5) for _ in range(5)])
student_3 = Student('третий', 47, [random.randint(1, 5) for _ in range(5)])
student_4 = Student('четвертый', 47, [random.randint(1, 5) for _ in range(5)])
student_5 = Student('пятый', 47, [random.randint(1, 5) for _ in range(5)])
student_6 = Student('шестой', 47, [random.randint(1, 5) for _ in range(5)])
student_7 = Student('седьмой', 47, [random.randint(1, 5) for _ in range(5)])
student_8 = Student('восьмой', 47, [random.randint(1, 5) for _ in range(5)])
student_9 = Student('девятый', 47, [random.randint(1, 5) for _ in range(5)])
student_10 = Student('десятый', 47, [random.randint(1, 5) for _ in range(5)])

student_list = [student_1, student_2, student_3, student_4, student_5, student_6,
                student_7, student_8, student_9, student_10]

for i_elem in student_list:  # NOTE хотим посмотреть студенческую ситуацию "до"
    print(i_elem.name, i_elem.summ())
print()

sorted_list = sorted(student_list, key=lambda x: x.summ())  # NOTE в Python 3.9 без круглых скобок не сработало

for i_elem in sorted_list:  # NOTE выводим более информативный ответ со студенческой ситуацией "после"
    print(i_elem.name, i_elem.summ())
