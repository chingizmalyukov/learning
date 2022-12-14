def singleton(cls):
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

# я даже пытаться не стал. со мной может кто-то позаниматься по этой теме, а то я ничего не понял,
# или мне и дальше гуглить?
# не думаю, это просто тема такая. Позаниматься с Вами может репетитор, но его поисками необходимо заняться самому.
# желаю успеха! И ещё бы пожелала так сильно на этой теме не зацикливаться.
# По мере необходимости у Вас будет возможность с ней разобраться подробнее.
