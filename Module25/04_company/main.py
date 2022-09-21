class Person:
    def __init__(self, name, surmane, age):
        self.set_name(name)
        self.set_surname(surmane)
        self.set_age(age)

    def set_name(self, name):
        self.__name = name

    def set_surname(self, surname):
        self.__surname = surname

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname


class Employee(Person):
    def payment(self):
        pass

    def __str__(self):
        return f'имя: {self.get_name()}, фамилия: {self.get_surname()}, з\п: {self.payment()}'


class Manager(Employee):

    def payment(self):
        return 13000


class Agent(Employee):
    __salles = 0

    def payment(self):
        return 5000 + self.get_salles() * 5 / 100

    def set_salles(self, salles):
        self.__salles = salles

    def get_salles(self):
        return self.__salles


class Worker(Employee):
    __hours = 0

    def payment(self):
        return 100 * self.get_hours()

    def set_hours(self, hours):
        self.__hours = hours

    def get_hours(self):
        return self.__hours


sallary_summ = 0

manager_1 = Manager('Tom', 'Mot', 20)
manager_2 = Manager('Kom', 'Kot', 30)
manager_3 = Manager('Fom', 'Fot', 40)
agent_1 = Agent('Tom', 'Mot', 20)
agent_2 = Agent('Kom', 'Kot', 30)
agent_3 = Agent('Fom', 'Fot', 40)
agent_1.set_salles(100)
agent_2.set_salles(100)
agent_3.set_salles(100)
worker_1 = Worker('Tom', 'Mot', 20)
worker_2 = Worker('Kom', 'Kot', 30)
worker_3 = Worker('Fom', 'Fot', 40)
worker_1.set_hours(10)
worker_2.set_hours(10)
worker_3.set_hours(10)

workers_list = [manager_1, manager_2, manager_3, agent_1, agent_2, agent_3, worker_1, worker_2, worker_3]

for human in workers_list:
    print(human)
