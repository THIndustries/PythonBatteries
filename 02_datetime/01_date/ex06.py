from datetime import date
from copy import deepcopy
from pprint import pprint

class CreateDict:

    def __new__(cls, *args, **kwargs):
        instance = super(CreateDict, cls).__new__(cls)
        instance.dct = {date(year=1945, month=5, day=i): [date(year=1945, month=5, day=i) for i in range(1, i+1)]
                        for i in range(1, 32)}
        return instance


my_date = CreateDict()

pprint(my_date.dct)
