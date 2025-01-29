import os

def get_only_dirs(path: str) -> None:
    count = 0
    for file in sorted(os.listdir(path)):
        if os.path.isdir(os.path.join(path, file)):
            print(file)
            count += 1

    print(count)

get_only_dirs('./')