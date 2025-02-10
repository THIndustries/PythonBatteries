import unittest
import random


def linear_search(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1


class TestLinearSearchFunction(unittest.TestCase):

    def test_zero_not_in(self):
        # test_numbers = random.sample(range(0,100), 5)
        test_numbers = [1, 4, 3, 4, 8]
        self.assertEqual(-1, linear_search(test_numbers, 0))


    def test_zero_in(self):
        test_numbers = [1, 4, 3, 4, 0]
        self.assertNotEqual(-1, linear_search(test_numbers, 0))
