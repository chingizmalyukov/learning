class Parent:
    child_list = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayinfo(self):
        print('\nname = {}\nage = {}\nchild_list = {}\n'.format(
            self.name, self.age, self.child_list))

    def calm_down(self, child):
        if child.rage:
            child.rage = False
            print('The child was calmed down!')
        else:
            print('Baby is calm!')

    def hungry_down(self, child):
        if child.hungry:
            child.hungry = False
            print('The baby was fed!')
        else:
            print('Baby already fed!')


class Child:
    def __init__(self, parent, name, age, rage=False, hungry=False):
        self.name = name
        self.age = age
        try:
            if age - parent.age <= 16:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print('Ошибка! Возраст ребенка должен быть меньше возраста'
                  ' родителя хотя бы на 16 лет!')
        parent.child_list.append(self.name)
        self.rage = rage
        self.hungry = hungry

    def baby_status(self):
        print('\nname = {}\nage = {}\nrage = {}\nhungry = {}'.format(
            self.name, self.age, self.rage, self.hungry
        ))


john = Parent('John', 34)
# baby = Child(john, 'Jo', 34)  # вариант в котором выдаст ошибку про возраст ребенка
jo = Child(john, 'Jo', 8, True, True)
john.sayinfo()
john.calm_down(jo)
john.hungry_down(jo)
jo.baby_status()
