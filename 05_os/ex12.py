import os
import stat        

def get_permissions(path):
    return stat.filemode(os.stat(path).st_mode)        


def change_permissions(path: str, mode: int) -> None:

    os.chmod(path, int(str(mode), 8))