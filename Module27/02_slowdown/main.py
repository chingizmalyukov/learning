import time
from typing import Callable, Any


def time_sleep(funct: Callable) -> Callable:
    """"Декоратор, который перед выполнением декорируемой функции ждёт несколько секунд"""

    # а каким образом можно выводить отсчет до старта?
    # пробовал через цикл, но он сразу вываливает все принты =(

    def wrapped_func(*args, **kwargs) -> Any:  # NOTE например, добавив декоратор =)
        for i_time in range(5, 0, -1):
            print(i_time, end=' ')
            time.sleep(1)
        print()
        return funct(*args, **kwargs)

    return wrapped_func


@time_sleep
def test() -> None:
    print('<здесь что-то происходит...>')


test()
