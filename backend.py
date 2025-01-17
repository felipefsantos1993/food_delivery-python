import os

restaurants = [{'name':'Super Burger', 'category':'fast food', 'active':False},
               {'name':'Sushi Bar', 'category':'japanese', 'active':False}]

def show_program_name():
    print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗██╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝██║
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░╚═╝
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗██╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝
""")

def show_program_options():
    print('1. Restaurant Registration')
    print('2. Restaurant List')
    print('3. Restaurant Status')
    print('4. Logout\n')

def stop_app():
    clean_subtitles('The program has been closed...')
    #back_to_mainly_menu()

def clean_subtitles(subtitle):
    os.system('cls')
    print(subtitle)
    print()

def back_to_the_mainly_menu():
    input('\n\n\nPress any button to return the mainly menu...\n')
    main()

def invalid_option():
    print('Invalid option!!!')
    main()

def restaurant_registration():
    clean_subtitles('New Restaurant')
    rn = input('What is the restaurant name?\n')
    rc = input('Whats is the restaurant category?\n')
    restaurants_data = {'name':rn, 'category': rc, 'active': False}
    restaurants.append(restaurants_data)
    print(f'\nThe restaurant {rn} has been registered!')
    back_to_the_mainly_menu()

def restaurant_list():
    clean_subtitles('List Of Restaurants')
    for r in restaurants:
        name = r['name']
        category = r['category']
        active = r['active']
        print(f'{name} | {category} | {active}')
    back_to_the_mainly_menu()

def restaurant_status():
    clean_subtitles('Insert the name of restaurant...')
    ra = input('Which restaurant would you like to change the status?\n')
    validation = False
    for r in restaurants:
        if r['name'] == ra:
            validation = not validation
            r['active'] = not r['active']
            message = f'\nThe restaurant {ra} has been activated!' if r['active'] else f'\nThe restaurant {ra} has been disabled!'
            print(message)
    if not validation:
        print(f'\nThe restaurant {ra} has not benn found!')
    back_to_the_mainly_menu()

def choose_option():
    try:
        option = int(input(f'Choose your option:\n'))
        #print(f'You have chosen {option}')1
        if option == 1:
            restaurant_registration()
        elif option == 2:
            restaurant_list()
        elif option == 3:
            restaurant_status()
        elif option == 4:
            stop_app()
    except:
        invalid_option()

#def choose_option_match():
#    option = int(input(f'Choose your option:\n'))
#    #print(f'You have chosen {option}')
#    match option:
#        case 1:
#            print(f'You have chosen: Register Restaurant')
#        case 2:
#            print('You have chosen: List Restaurant')
#        case 3:
#            print('You have chosen: Active Restaurant')
#        case _:
#            print(f'...')

def main():
    os.system('cls')
    show_program_name()
    show_program_options()
    choose_option()

if __name__ == '__main__':
    main()