import logging
import os

# logging.basicConfig(level=logging.DEBUG)
my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
my_logger.addHandler(handler)

class RenameFiles:

    def __init__(self, path_folder):
        self.my_path_folder = path_folder
        my_logger.log(logging.DEBUG, f'Объект {self.__class__.__name__} был успешно создан')

    @property
    def my_path_folder(self):
        my_logger.log(logging.DEBUG, 'Geter-декоратор работает...')
        return self.__path_folder

    @my_path_folder.setter
    def my_path_folder(self, new_path_folder):
        if isinstance(new_path_folder, str):
            my_logger.log(logging.DEBUG, 'Setter-декоратор работает...')
            self.__path_folder = new_path_folder
        else:
            my_logger.log(logging.ERROR, 'Вы передали не строку')
            raise ValueError(f'Ожидалась строка, но получен другой тип данных - {type(new_path_folder)}')  # Остановка выполнения





    def rename_files(self):
        pass



if __name__ == '__main__':
    try:
        obj1 = RenameFiles('1')
    except ValueError as e:
        my_logger.log(logging.WARNING, f'Ошибка при создании объекта: {e}')
