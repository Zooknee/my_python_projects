def get_name():
    name = input('Enter your name: ')
    return name

def greet_user():
    user = get_name()
    print(f'Hello {user}, welcome to the interactive program!')

greet_user()


def get_age():
    age = int(input('Enter your age: '))
    return age

def age_check():
    user_age = get_age()
    if user_age >= 18:
        print('You are an adult.')
    else:
        print('You are a minor.')

age_check()


def main():
    user_name = get_name()
    user_age = get_age()
    print(f'{user_name}, you are {user_age} years old.')
    if user_age >= 18:
        print('Access granted.')
    else:
        print('Access denied.')

main()
