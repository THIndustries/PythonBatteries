import os
import stat

def get_permissions(path_way: str) -> str:
    file_info = os.stat(path_way)
    return stat.filemode(file_info.st_mode)

print(get_permissions('ex10.py'))