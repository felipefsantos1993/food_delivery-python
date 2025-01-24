from models.menu.item import Item

class Food(Item):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description = description
