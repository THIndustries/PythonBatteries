from collections import UserList

# Напишите определение класса MyList
class MyList(UserList):

    def shift_left(self):
        self.data = self.data[1:]+[self.data[0]]

    def shift_right(self):
        self.data = [self.data[-1]]+self.data[:-1]

    def for_each(self, function):
        self.data = [function(value) for value in self.data]


my_list = MyList([1, 2, 3, 4, 5])

assert my_list.data == [1, 2, 3, 4, 5]

my_list.shift_left()
assert my_list.data == [2, 3, 4, 5, 1]
my_list.shift_left()
my_list.shift_left()
assert my_list.data == [4, 5, 1, 2, 3]

my_list.shift_right()
assert my_list.data == [3, 4, 5, 1, 2]

my_list.for_each(lambda x: x ** 2)
assert my_list.data == [9, 16, 25, 1, 4]