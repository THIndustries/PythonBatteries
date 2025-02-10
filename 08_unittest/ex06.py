import unittest


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_reading_time(self):
        return f"{self.pages * 1.5} minutes"

    def apply_discount(self, discount):
        if not isinstance(discount, float):
            raise ValueError('Discount must be float number')
        if 0 <= discount <= 1:
            discounted_price = self.price - (discount * self.price)
            return f"${discounted_price}"
        raise ValueError('Discount must be float number between 0 and 1')


class TestBookClass(unittest.TestCase):
    def test_init_method(self):
        book = Book('title', 'author', 200, 30)
        self.assertEqual(book.title, 'title')
        self.assertEqual(4, len(book.__dict__))

    def test__str__method(self):
        book = Book('title', 'author', 200, 30)
        self.assertEqual(str(book), f'{book.title} by {book.author}')

    def test_get_reading_time(self):
        book = Book('title', 'author', 200, 30)
        self.assertEqual(book.get_reading_time(), "300.0 minutes")

    def test_apply_discount_not_float(self):
        book = Book('title', 'author', 200, 30)
        with self.assertRaises(ValueError):
            book.apply_discount("2")

    def test_apply_discount_more_than_1(self):
        book = Book('title', 'author', 200, 30)
        with self.assertRaises(ValueError):
            book.apply_discount(1.2)

    def test_apply_discount_less_than_0(self):
        book = Book('title', 'author', 200, 30)
        with self.assertRaises(ValueError):
            book.apply_discount(-0.5)

    def test_apply_discount_good_case(self):
        book = Book('title', 'author', 200, 30)
        self.assertEqual(book.apply_discount(0.2), "$24.0")