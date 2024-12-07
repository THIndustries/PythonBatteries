from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float


class ShoppingCart:

    def __init__(self):
        self._items = list()
        self._total_price = None


    def add_item(self, item):
        if isinstance(item, Product):
            self._items.append(item)
            self._total_price = None

    def remove_item(self, item):
        if self._items:
            self._items.remove(item)
            self._total_price = None
        else:
            raise ValueError

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(len(self._items))

    @property
    def total_price(self):
        if self._total_price is None:
            self._total_price = sum(item.price for item in self._items)
        return self._total_price



    @property
    def items(self):
        return sorted(self._items, key=lambda x: (x.price, x.name))




apple = Product("Apple", 1.5)
banana = Product("Banana", 0.75)
chocolate = Product("Chocolate", 2.99)

cart = ShoppingCart()
cart.add_item(banana)
cart.add_item(apple)
cart.add_item(chocolate)

assert len(cart) == 3
assert cart.items == [banana, apple, chocolate]

milk = Product('Milk', 1)
cart.add_item(milk)
assert cart.items == [banana, milk, apple, chocolate]
print("Items in the cart:", [item.name for item in cart.items])
print("Total price:", cart.total_price)
assert cart.total_price == 6.24
cart.add_item(banana)
assert len(cart) == 5
assert cart.total_price == 6.99
cart.remove_item(milk)
assert len(cart) == 4
cart.remove_item(banana)
cart.remove_item(banana)
assert len(cart) == 2
try:
    cart.remove_item(banana)
except ValueError:
    pass