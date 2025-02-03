import logging

log_format = "%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(lineno)d:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_format)
file_handler = logging.FileHandler('analyze_data.log')
logger = logging.getLogger(__name__)
logger.addHandler(file_handler)

def analyze_data(data_file):
    logger.log(logging.DEBUG, "Начало анализа данных")
    try:
        with open(data_file, 'r') as file:
            data = file.read()
            logger.log(logging.INFO, data)
        logger.log(logging.DEBUG, 'Анализ успешно завершен')
    except FileNotFoundError:
        logger.log(logging.ERROR, f'"Файл не найден: %s", {data_file}')
    except Exception as e:
        logger.log(logging.ERROR, f"Произошла ошибка при анализе данных: %s", {str(e)})



if __name__ == "__main__":
    data_file = r""
    analyze_data(data_file)