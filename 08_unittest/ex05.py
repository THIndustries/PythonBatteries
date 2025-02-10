import unittest
from check_list import is_sorted_ascending, is_sorted_descending


class CheckListTestCase(unittest.TestCase):

    def test_is_sorted_false(self):
        arr = [3, 2, 4, 1, 4, 3]
        self.assertEqual(is_sorted_ascending(arr), False)

    def test_is_sorted_true(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(is_sorted_ascending(arr), True)

    def is_sorted_descending_false(self):
        arr = [2, 2, 3, 4, 5]
        self.assertEqual(is_sorted_descending(arr), False)

    def is_sorted_descending_true(self):
        arr = [6, 3, 2, 0]
        self.assertEqual(is_sorted_descending(arr), True)
