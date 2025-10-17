def greet_user():
    print("Welcome to week 3!")
    print("You're learning Python functions." )

greet_user()

def greet_person(name):
    print("Hello,", name)
    print("Welcome back to python!")

greet_person("Isaiah")
greet_person("Zooknee")

def add_numbers(a, b):
    total = a + b
    print("The sum of", a, "and", b, "is:", total)

add_numbers(3, 7)
add_numbers(12, 5)


def multiply(a, b):
    return a * b

product = multiply(4, 5)
print("The product is:", product)


def calculate_rectangle_area(w, l):
    return w * l

area = calculate_rectangle_area(6, 8)
print("The area of the rectangle is:", area)


import os

def system_check():
    print("Running system check...")
    os.system("uname -a")
    os.system("df -h | head -5")

system_check()
