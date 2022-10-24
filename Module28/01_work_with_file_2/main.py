import os


class File:
    """Контекст-менеджер:
        1)при попытке открыть несуществующий файл,
     автоматически создаёт и открывает этот файл в режиме записи
        2)на выходе из менеджера подавляются все исключения, связанные с файлами."""

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self):
        if os.path.exists(self.file_name):
            self.file = open(self.file_name, 'r', encoding='utf-8')
        else:
            self.file = open(self.file_name, 'a', encoding='utf-8')

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


with File(file_name='test.txt') as test:
    for i_string in test:  # для проверки подавления исключений
        print(i_string)
