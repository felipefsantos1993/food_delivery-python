from models.backend_POO import Restaurants

super_burger = Restaurants('Super Burger', 'Fast Food')
hot_chili_peppers = Restaurants('Hot Chili Peppers', 'Mexican')
sushi_bar = Restaurants('Sushi Bar', 'Japanese')




def main():
    Restaurants.restaurant_list()

if __name__ == '__main__':
    main()