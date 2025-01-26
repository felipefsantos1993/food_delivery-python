from models.restaurants import Restaurants
from models.assessments import Assessments
from models.menu.food import Food
from models.menu.drink import Drink
from models.menu.item import Item

#hot_chili_peppers = Restaurants('Hot Chili Peppers', 'Mexican')
#sushi_bar = Restaurants('Sushi Bar', 'Japanese')
super_burger = Restaurants('Super Burger', 'Fast Food')
orange_juice = Drink('Orange Juice', 2.00, 'M')
hamburger = Food('Hamburger', 10.00, 'The best hamburger of the town...')

super_burger.add_menu(orange_juice)
super_burger.add_menu(hamburger)
super_burger.get_assesment('Felipe', 5)
super_burger.get_assesment('Manu', 5)
super_burger.get_assesment('Lu', 4.5)

def main():
    print(orange_juice)
    print(hamburger)

if __name__ == '__main__':
    main()