users = {}

def add_user(name, age):
    users[name] = age
    return f'User {name} added successfully.'

def view_users():
    if not users:
        return 'No users found.'
    result = 'Current users:\n'
    for name, age in users.items():
        result += f' - {name}, age {age}\n'
    return result

def remove_user(name):
    if name in users:
        del users[name]
        return f'User {name} removed.'
    else:
        return f'User {name} not found.'

