import os

restaurants = [{'nome':'Sushi Bar', 'categoria':'japonesa', 'ativo':False},
               {'nome':'Super Burger', 'categoria':'fast food', 'ativo':True},
               {'nome':'Cantina da Nona', 'categoria':'italiana', 'ativo':True}]

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
    clean_subtitles('The program has been finished...')
    #back_to_mainly_menu()

def clean_subtitles(subtitle):
    os.system('cls')
    print(subtitle)
    print()

def back_to_mainly_menu():
    input('\n\n\nPress any button to return the mainly menu...\n')
    main()

def invalid_option():
    print('Invalid option!!!')
    main()

def restaurant_register():
    clean_subtitles('New Restaurants')
    rn = input('What is the restaurant name?\n')
    restaurants.append(rn)
    print(f'The restaurant {rn} has been registered!')
    back_to_mainly_menu()

def restaurant_list():
    clean_subtitles('List Of Restaurants')
    for r in restaurants:
        name = r['nome']
        category = r['categoria']
        active = r['ativo']
        print(f'{name} | {category} | {active}')
    back_to_mainly_menu()

def choose_option():
    try:
        option = int(input(f'Choose your option:\n'))
        #print(f'You have chosen {option}')1
        if option == 1:
            restaurant_register()
        elif option == 2:
            restaurant_list()
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