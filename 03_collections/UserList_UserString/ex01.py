from collections import UserString


class StringDeque(UserString):

    def appendleft(self, symbol):
        if StringDeque.check_symbol(symbol):
            self.data = symbol+self.data

    def append(self, symbol):
        if StringDeque.check_symbol(symbol):
            self.data = self.data+symbol

    @staticmethod
    def check_symbol(symbol):
        if type(symbol) != str or len(symbol) != 1:
           raise ValueError
        return True


deque = StringDeque("abc")

assert type(deque) == StringDeque
deque.appendleft("d")
assert deque.data == 'dabc'
deque.append("e")
assert deque.data == 'dabce'

try:
    deque.append(123)
except ValueError:
    pass

try:
    deque.append('hello')
except ValueError:
    pass

try:
    deque.append('')
except ValueError:
    pass

try:
    deque.appendleft([1])
except ValueError:
    pass

try:
    deque.appendleft('hi')
except ValueError:
    pass