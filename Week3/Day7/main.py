import user_tools

def main():
    while True:
        print('\n--- User Management Menu ---')
        print('1. Add user')
        print('2. View users')
        print('3. Remove user')
        print('4. Quit')

        choice = input('Choose an option: ')

        if choice == '1':
            name = input('Enter name: ')
            age = int(input('Enter age: '))
            print(user_tools.add_user(name, age))

        elif choice == '2':
            print(user_tools.view_users())

        elif choice == '3':
            name = input('Enter name to remove: ')
            print(user_tools.remove_user(name))

        elif choice == '4':
            print('Exiting program...')
            break

        else:
            print('Invalid option. Please try again.')

main()
