import os


def check(start_path):
    for i_elem in os.listdir(start_path):
        path = os.path.join(start_path, i_elem)
        if os.path.isfile(path) or os.path.islink(path):
            result['file_count'] += 1
            result['size'] += os.path.getsize(path)
        elif os.path.isdir(path):
            result['dir_count'] += 1
            check(path)


result = {'size': 0,
          'dir_count': 0,
          'file_count': 0}

start_path = input('Укажите путь к папке: ') #'X:\GIT\python_basic\Module14'
check(start_path)

print(f'Размер каталога (в Кб): {result["size"]}')
print(f'Количество подкаталогов: {result["dir_count"]}')
print(f'Количество файлов: {result["file_count"]}')