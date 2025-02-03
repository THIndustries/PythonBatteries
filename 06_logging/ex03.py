import logging

my_logger = logging.getLogger(__name__)
my_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log_file_for_test.log')
my_logger.setLevel(logging.DEBUG)
my_logger.addHandler(my_handler)
my_logger.addHandler(file_handler)

def division():
    my_logger.debug('Начинаем делить!')
    try:
        dividend = float(input('Введите делимое: '))
        divisor = float(input('Введите делитель: '))
    except ValueError as er:
        my_logger.log(logging.CRITICAL, f"Введены не числовые значения - {er}")
    except ZeroDivisionError:
        my_logger.error("Делишь на ноль")
    else:
        my_logger.info(f'Полученный результат {dividend} / {divisor} = {dividend / divisor}')
        return dividend / divisor


if __name__ == '__main__':
    result = division()

