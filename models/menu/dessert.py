from models.menu.item import Item

class Dessert(Item):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type
    
    def __str__(self):
        return self._name
    
    def apply_discount(self):
        self._price -= (self._price * 0.02)
