import time
from typing import Callable
import functools


def time_sleep(funct: Callable) -> Callable:
    """"Декоратор, который перед выполнением декорируемой функции ждёт несколько секунд"""

    # а каким образом можно выводить отсчет до старта?
    # пробовал через цикл, но он сразу вываливает все принты =(

    time.sleep(3)
    return funct


@time_sleep
def test() -> None:
    print('<здесь что-то происходит...>')


test()
