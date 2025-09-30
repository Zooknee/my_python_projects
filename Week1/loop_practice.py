for i in range(11):
	print("This is loop number", i)

for i in range(10, 0, -1):
	print("Countdown:", i)

for i in range(1, 6):
	if i == 3:
	    continue
	print("Continue example:", i)

for i in range(1, 4):	
    for j in range(1, 4):
    	print(i, "x", j, "=", i * j)

x = 1
while x <= 10:
    print("While loop count:", x)
    x += 1

user_input = ""
while user_input != "quit":
    user_input = input("Type something (or 'quit' to stop): ")
    if user_input != "quit":
        print("You typed:", user_input)
    