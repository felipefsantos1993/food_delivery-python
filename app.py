from models.restaurants import Restaurants
from models.assessments import Assessments
from models.menu.food import Food
from models.menu.drink import Drink
from models.menu.dessert import Dessert
from models.menu.item import Item

#hot_chili_peppers = Restaurants('Hot Chili Peppers', 'Mexican')
#sushi_bar = Restaurants('Sushi Bar', 'Japanese')
super_burger = Restaurants('Super Burger', 'Fast Food')

orange_juice = Drink('Orange Juice', 2.00, 'M')
orange_juice.apply_discount()

hamburger = Food('Hamburger', 10.00, 'The best hamburger of the town...')
hamburger.apply_discount()

apple_pie = Dessert('Apple Pie', 15.00, 'Pies')
apple_pie.apply_discount()

super_burger.add_menu(orange_juice)
super_burger.add_menu(hamburger)
super_burger.add_menu(apple_pie)
super_burger.get_assesment('Felipe', 5)
super_burger.get_assesment('Manu', 5)
super_burger.get_assesment('Lu', 4.5)

def main():
    super_burger.menu_list

if __name__ == '__main__':
    main()