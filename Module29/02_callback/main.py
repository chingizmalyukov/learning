app = {}


def callback(route):
    def wrapper(func):
        app[route] = func

        def wrapped():
            ret = func()
            return ret

        return wrapped

    return wrapper


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
# я списал это задание, но я НЕ понимаю как это работает! функция example не вызывается нигде в коде.
# да, "прямиком" она нигде не вызывается, но, при этом срабатывает - это мы видим в консоли
# и тут это можно назвать "магией" декораторов. Весьма необычно, но с практикой и опытом работы с ними станет проще
