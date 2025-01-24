from models.restaurants import Restaurants
from models.assessments import Assessments
from models.menu.food import Food
from models.menu.drink import Drink

super_burger = Restaurants('Super Burger', 'Fast Food')
orange_juice = Drink('Orange Juice', 10.50, 'M')
hamburger = Food('Hamburger', 35.20, 'A delicius hamburger...')




#super_burger.get_assesment('Felipe', 5)
#super_burger.get_assesment('Manu', 5)
#super_burger.get_assesment('Lu', 4.5)

#hot_chili_peppers = Restaurants('Hot Chili Peppers', 'Mexican')
#sushi_bar = Restaurants('Sushi Bar', 'Japanese')




def main():
    pass

if __name__ == '__main__':
    main()