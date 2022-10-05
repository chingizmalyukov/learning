import os


def file_generator(start_path, search_path):
    for i_elem in os.listdir(start_path):
        path = os.path.join(start_path, i_elem)
        if os.path.isfile(path) or os.path.islink(path):
            print(path)
        else:
            if i_elem == search_path:
                return
            else:
                file_generator(path, search_path)


start_path = input('Директория начала поиска: ')
search_path = input('Имя искомой директории: ')

file_generator(start_path, search_path)
