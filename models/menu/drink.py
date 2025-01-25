from models.menu.item import Item

class Drink(Item):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return self._name