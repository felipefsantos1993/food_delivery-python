import os

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
    print('1. Register Restaurant')
    print('2. List Restaurant')
    print('3. Actve Restaurant')
    print('4. Logout')

def stop_app():
    os.system('cls')
    print('The program has been finished...\n')

def invalid_option():
    input('Press any button to return...')
    os.system('cls')
    main()

def choose_option():
    try:
        option = int(input(f'Choose your option:\n'))
        #print(f'You have chosen {option}')
        if option == 1:
            print(f'You have chosen: Register Restaurant')
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