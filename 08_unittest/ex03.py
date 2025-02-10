import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Ingredient:
    def __init__(self, name, weight, price):
        logger.log(logging.DEBUG, '__init__ Ingredient is working...')
        self.name = name
        self.weight = weight
        self.price = price  # стоимость за 100гр
        self.__cost = None

    @property
    def cost(self):
        if self.__cost is None:
            self.__cost = (self.price * self.weight) / 100
        return self.__cost


class Pizza:
    def __init__(self, name, ingredients=None):
        logger.log(logging.DEBUG, '__init__ Pizza is working...')
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients
        self.__cost = None


    @property
    def cost(self):
        if self.__cost is None:
            self.__cost = sum(ingr.cost for ingr in self.ingredients) + 100
        return self.__cost




