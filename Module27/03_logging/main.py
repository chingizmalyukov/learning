from typing import Callable, Any
from datetime import datetime
import functools


def logging(funct: Callable) -> Callable:
    """"Декоратор отвечающий за логирование функции."""

    @functools.wraps(funct)
    def dec(*args, **kwargs) -> Any:
        try:

            funct(*args, **kwargs)
            print('Функция {name} выполнилась!'.format(name=funct.__name__))
            return funct(*args, **kwargs)
        except Exception as error:
            error_text = error
            # как убрать миллисекунды в выводе времени?
            # например, воспользовавшись функцией time.strftime('%d.%m.%Y %H:%M:%S') и вместо этого записать её без :%S
            message = ('{time}: Функция {name} не выполнилась! \nтекст ошибки: {error}'.format(
                time=datetime.now(),
                name=funct.__name__,
                error=error_text))
            print(message)
            with open('errors.txt', 'a', encoding='utf-8') as error_log:
                error_log.write(message)
                error_log.write('\n')
            return 'ошибка'

    return dec


@logging
def some_action(num: int) -> int:
    result = 1 // num
    return result


number = [1, 2, 0, 3, 'lol', 4]

for i_num in number:
    print('ответ:', some_action(i_num))
