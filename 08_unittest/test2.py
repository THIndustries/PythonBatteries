import logging
import unittest
from ex03 import Pizza, Ingredient, logger

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.chicken = Ingredient('chicken', 200, 80)
        self.mozzarella = Ingredient('mozzarella', 300, 110)
        self.sauce_bbq = Ingredient('sauce bbq', 150, 70)
        self.red_onion = Ingredient('red onion', 150, 50)

        self.barbecue = Pizza('BBQ', [self.chicken, self.mozzarella, self.sauce_bbq, self.red_onion])

    def test_initial_objects(self):
        self.assertEqual(self.chicken.name, 'ch1icken')
        logger.log(level=logging.DEBUG, msg='test_initial_objects отработал успешно')


if __name__ == '__main__':
    try:
        unittest.main()
    except AssertionError as e:
        logger.log(level=logging.ERROR, msg=f'Ошибка ')