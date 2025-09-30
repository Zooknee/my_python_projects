num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)
print("Difference =", num1 - num2)

if num1 > num2:
    print("The bigger number is", num1)
elif num2 > num1:
    print("The bigger number is", num2)
else:
    print("Both numbers are equal")