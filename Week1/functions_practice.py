def greet(name):
    print("Hello from a function,",name)

def add (a, b): 
    return a + b

greet("Isaiah")
print(add(3, 5))

def multiply (a, b):
    return a * b

print(multiply(4, 6))

def grade_checker(score):  
    if score >= 60:
        return "Pass"
    else:  
        return "Fail"

print(grade_checker(43))
print(grade_checker(89))
    
