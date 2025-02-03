import logging

logger = logging.getLogger('my_log')
handler = logging.FileHandler('log_file.log')
logger.addHandler(handler)
logger.setLevel('DEBUG')

logger.info('Шибка')