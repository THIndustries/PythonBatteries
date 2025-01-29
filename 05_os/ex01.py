import os

def is_dir_empty(path: str) -> bool:
    return not os.listdir(path)

print(is_dir_empty('./files'))