username = 'Zooknee'

def greet():
    username = 'Isaiah'
    print('Inside function:', username)

greet()
print('Outside function:', username)

import os

def get_system_name():
    stream = os.popen('hostname')
    return stream.read().strip()

def show_system_info():
    name = get_system_name()
    print('System name detected:', name)

show_system_info()
