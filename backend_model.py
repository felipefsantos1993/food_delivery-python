import os

restaurants = [{'name':'super burger', 'category':'fast food', 'status':False},
               {'name':'sushi bar', 'category':'japanese', 'status':False}]

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
    print('1. RESTAURANT REGISTRATION')
    print('2. RESTAURANT LIST')
    print('3. RESTAURANT STATUS')
    print('4. LOGOUT\n')

def stop_app():
    clean_subtitles('The program has been closed...')
    #back_to_mainly_menu()

def clean_subtitles(subtitle):
    os.system('cls')
    text = '=' * len(subtitle)
    print(text)
    print(subtitle)
    print(text)
    print()

def back_to_the_mainly_menu():
    input('\n\n\nPress any button to return the mainly menu...\n')
    main()

def invalid_option():
    print('Invalid option!!!')
    main()

def restaurant_registration():
    '''This function does...
    INPUTS:
    - name
    
    '''
    clean_subtitles('NEW RESTAURANT')
    rn = input('What is the restaurant name?\n')
    rc = input('Whats is the restaurant category?\n')
    restaurants_data = {'name':rn, 'category': rc, 'status': False}
    restaurants.append(restaurants_data)
    print(f'\nThe restaurant {rn} has been registered!')
    back_to_the_mainly_menu()

def restaurant_list():
    clean_subtitles('LIST OF RESTAURANTS')
    header = f'{'NAME'.ljust(20)} | {'CATEGORY'.ljust(20)} | {'STATUS'.ljust(20)}'
    print(f'{header}\n')
    for r in restaurants:
        name = r['name']
        category = r['category']
        status = 'active' if r['status'] else 'deactive'
        print(f'{name.ljust(20)} | {category.ljust(20)} | {status.ljust(20)}')
    back_to_the_mainly_menu()

def restaurant_status():
    clean_subtitles('RESTAURANT STATUS')
    ra = input('Which restaurant would you like to change the status?\n')
    validation = False
    for r in restaurants:
        if r['name'] == ra:
            validation = not validation
            r['active'] = not r['active']
            message = f'\nThe restaurant {ra} has been activated!' if r['active'] else f'\nThe restaurant {ra} has been deactivated!'
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