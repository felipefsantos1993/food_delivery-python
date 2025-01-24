from models.menu.item import Item

class Drink(Item):
    def __init__(self, name, price, size):
        super().__dir__(name, price)
        self._size = size