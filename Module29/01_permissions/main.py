from typing import Callable


def check_permission(user: str) -> Callable:
    def check_access(funct: Callable) -> Callable:
        def wrapped_funct(*args, **kwargs) -> None:
            if user_permissions[0] == user:
                funct(*args, **kwargs)
            else:
                print(f'PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {funct.__name__}')
            return

        return wrapped_funct

    return check_access


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
