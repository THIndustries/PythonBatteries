import os


def get_dir_files(path):
    for file in os.listdir(path):
        print(file)


get_dir_files('./files')