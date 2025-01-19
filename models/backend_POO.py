class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234



class Restaurants:
# "self" can be any word

    restaurant = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._status = False
        Restaurants.restaurant.append(self)

    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def restaurant_list(cls):
        print(f'{'name'.ljust(25)} | {'category'.ljust(25)} | {'status'}')
        for r in cls.restaurant:
            print(f'{r._name.ljust(25)} | {r._category.ljust(25)} | {r.restaurant_status}')

    @property
    def restaurant_status(self):
        return 'active' if self._status else 'deactive'
    
    def change_restaurant_status(self):
        self._status = not self._status
    
super_burger = Restaurants('super burger', 'fast food')
pizza_supreme = Restaurants('PIZZA supreme', 'ItaliAN')
super_burger.change_restaurant_status()

Restaurants.restaurant_list()