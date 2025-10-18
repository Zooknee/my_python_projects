def greet(name):
    print(f'Hello {name}, welcome to Python!')

greet('Zooknee')

def greet_with_time(name, time_of_day):
    print(f"Good {time_of_day}, {name}! Hope you're doing great.")

greet_with_time('Zooknee', 'afternoon')


def greet_default(name='friend'):
    print(f'Hello {name}, nice to meet you!')

greet_default()
greet_default('Zooknee')


def add_numbers(a, b):
    return a + b

sum_result = add_numbers(5, 7)
print(f'The sum is {sum_result}.')

def subtract_numbers(a, b):
    return a - b

result = subtract_numbers(10, 4)
print(result)
