# Напишите определение класса Stack
class EmptyStackError(BaseException):
    pass

class Stack:

    def __init__(self):
        self.arr = list()

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        if self.arr:
            return self.arr.pop()
        else:
            raise EmptyStackError

    def peek(self):
        return self.arr[-1]

    def is_empty(self):
        return not self.arr

    @property
    def size(self):
        return len(self.arr)

# Проверки стека
my_stack = Stack()
assert my_stack.size == 0
assert my_stack.is_empty()
my_stack.push('A')
my_stack.push('W')
my_stack.push('M')
assert my_stack.size == 3
assert not my_stack.is_empty()
assert my_stack.pop() == 'M'

assert my_stack.peek() == 'W'
assert my_stack.pop() == 'W'

assert my_stack.peek() == 'A'
my_stack.push('hello')
assert my_stack.size == 2

assert my_stack.pop() == 'hello'
assert my_stack.pop() == 'A'
assert my_stack.is_empty()

try:
    my_stack.pop()
except EmptyStackError:
    pass