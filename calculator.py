num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
	print("The result is", num1 + num2)
elif operation == "-":
	print("The result is", num1 - num2)
elif operation == "*":
	print("The result is", num1 * num2)
elif operation =="/":
	print("The result is", num1 / num2)
else:
	print("Invalid operation")
