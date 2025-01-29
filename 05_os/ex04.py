import os

class FileCount:


    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return len(os.listdir(instance.path))

class Folder:
    count = FileCount()

    def __init__(self, user_path):
        self.path = user_path


folder_include = Folder('include')
assert folder_include.count == 4

folder_nested = Folder('nested')
assert folder_nested.count == 3

print('Good')