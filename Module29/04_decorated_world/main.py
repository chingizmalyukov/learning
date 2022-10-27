def decorator_with_args_for_any_decorator(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func, *args, **kwargs):
    def wrapper(text, num):
        print("Переданные арги и кварги в декоратор:", args, kwargs)
        return func(text, num)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


decorated_function("Юзер", 101)
# эту задачу я тоже не смог сразу решить. пришлось читать\смотреть разборы,
# у меня вопрос: это задача сложная, или за 5, примерно 8 минутных ролика,
# нереально объяснить эту тему?
# думаю, ей (этой темой) нужно проникнуться и "набить руку" на решении задач
# а объяснить исчерпывающе - действительно необычайно сложно
