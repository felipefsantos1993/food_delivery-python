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

#"self" can be any word
class Restaurants:
    restaurant = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.status = False
        Restaurants.restaurant.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'
    def restaurant_list():
        for r in Restaurants.restaurant:
            print(f'{r.name} | {r.category} | {r.status}')
    
super_burger = Restaurants('Super Burger', 'Fast Food')
Restaurants.restaurant_list()