import helpers

app_name = 'PythonScopeApp'

def show_app():
    version = '1.0'
    print(f'{app_name} version {version}')

def change_name():
    app_name = 'NewAppName'
    print(f'Inside function, app_name is {app_name}')

show_app()
change_name()
print(f'Outside functionk app_name is still {app_name}')

print(helpers.greet_user('Zooknee'))
print(f'The square of 5 is {helpers.square(5)}')
