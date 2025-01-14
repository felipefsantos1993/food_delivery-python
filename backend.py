import os

restaurants = []

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
    print('1. Restaurant Register')
    print('2. Restaurant List')
    print('3. Restaurant Actve')
    print('4. Logout\n')

def stop_app():
    os.system('cls')
    print('The program has been finished...')

def invalid_option():
    input('Press any button to return the mainly menu...\n')
    os.system('cls')
    main()

def restaurant_register():
    os.system('cls')
    print('New Restaurants\n')
    rn = input('What is the restaurant name?\n')
    restaurants.append(rn)
    print(f'The restaurant {rn} has been registered!\n\n\n')
    input('Press any button to return the mainly menu...\n')
    main()

def choose_option():
    try:
        option = int(input(f'Choose your option:\n'))
        #print(f'You have chosen {option}')1
        if option == 1:
            restaurant_register()
        elif option == 2:
            print('You have chosen: List Restaurant')
        elif option == 3:
            print('You have chosen: Active Restaurant')
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