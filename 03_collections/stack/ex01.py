# Напишите определение класса Queue
class Queue:

    def __init__(self):
        self.arr = list()

    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        if self.arr:
            return self.arr.pop(0)
        else:
            raise IndexError

    def peek(self):
        return self.arr[0]


    def is_empty(self):
        return not self.arr

    @property
    def size(self):
        return len(self.arr)

# Проверки очереди
my_queue = Queue()

assert my_queue.size == 0
assert my_queue.is_empty()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
assert my_queue.size == 3
assert not my_queue.is_empty()
assert my_queue.dequeue() == 1

assert my_queue.peek() == 2
assert my_queue.dequeue() == 2

assert my_queue.peek() == 3
my_queue.enqueue('hello')
assert my_queue.size == 2

assert my_queue.dequeue() == 3
assert my_queue.dequeue() == 'hello'
assert my_queue.is_empty()

try:
    my_queue.dequeue()
except IndexError:
    pass