from math import factorial
from collections import UserDict

class ExtraDict(UserDict):
    def map(self, func):
        for k, v in self.data.items():
            self.data[k] = func(v)

    def remove(self, key):
        if key in self.data:
             self.data.__delitem__(key)
        else:
            raise KeyError

    def is_empty(self):
        return False if self.data else True

my_dict = ExtraDict({'a': 1, 'b': 2, 'c': 3})
print("Original dictionary:", my_dict.data)

my_dict.map(lambda x: x * 2)
print("Dictionary after applying 'map':", my_dict.data)

my_dict.map(factorial)
print("Dictionary after applying factorial:", my_dict.data)

my_dict.remove('b')
my_dict.pop('c')

assert not my_dict.is_empty()

my_dict.remove('a')

assert my_dict.is_empty()

try:
    my_dict.remove('a')
except KeyError:
    pass