from typing import Callable, Any
import functools


def debug(function: Callable) -> Callable:
    """Декоратор, который при каждом вызове декорируемой функции выводит её имя,
     а затем — какое значение она возвращает. После этого выводится результат её выполнения."""

    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> Any:
        print("Вызывается {}({})".format(
            function.__name__,
            ", ".join(
                list(f"\"{arg}\""
                     if isinstance(arg, str) else
                     str(arg) for arg in args)
                +
                list(f"{k}=\"{v}\""
                     if isinstance(v, str) else
                     f"{k}={v}" for k, v in kwargs.items())
            )
        ))
        result = function(*args, **kwargs)
        print("'{}' вернула значение'{}'".format(
            function.__name__, result
        ))
        print(result + '\n')
        return result

    return wrapper


@debug
def greeting(name: str, age: int = None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# Совет: попробуйте самостоятельно изучить функцию repr. Это поможет в решении задачи.(c)
# я почитал, но не понял как он работает. по этому пошел по длинному пути)
