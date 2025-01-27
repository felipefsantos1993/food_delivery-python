from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @abstractmethod
    def apply_discount(self):
        pass
