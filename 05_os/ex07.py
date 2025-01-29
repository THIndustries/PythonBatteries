import os
from datetime import datetime
from pprint import pprint

curr_way = r'D:\ff'

def show_file_info(path):
    result = {}
    for file in os.listdir(path):
        curr_file_time = os.path.getatime(os.path.join(path, file))
        readable_time = datetime.fromtimestamp(curr_file_time).strftime('%Y-%m-%d %H:%M:%S')
        result[file] = f'время - {readable_time}'

    return result

pprint(show_file_info(curr_way))


