import functools
from typing import Callable

list_num = [0]


def counter(function: Callable) -> Callable:
    """"Декоратор counter, считающий и выводящий количество вызовов декорируемой функции"""

    # Посмотрел в следующей теме разбор последней задачи из ДЗ.
    # Сделал также. Потом закомментил и придумал свое решение,
    # используя знания о списках. Кто молодец? Я - молодец.
    # Супер! :)
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        list_num[0] += 1
        # wrapper.count += 1
        function(*args, **kwargs)
        print('Функция {name} была использована {wrapper_count} раз.'.format(
            name=function.__name__,
            wrapper_count=list_num[0]  # wrapper.count
        ))
        return test

    # wrapper.count = 0
    return wrapper


@counter
def test() -> None:
    print('Что-то происходит')


for _ in range(3):
    test()
