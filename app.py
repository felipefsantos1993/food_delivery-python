from models.restaurants import Restaurants
from models.assessments import Assessments

super_burger = Restaurants('Super Burger', 'Fast Food')
super_burger.get_assesment('Felipe', 10)
super_burger.get_assesment('Manu', 6)
super_burger.get_assesment('Lu', 3)



#hot_chili_peppers = Restaurants('Hot Chili Peppers', 'Mexican')
#sushi_bar = Restaurants('Sushi Bar', 'Japanese')




def main():
    Restaurants.restaurant_list()

if __name__ == '__main__':
    main()