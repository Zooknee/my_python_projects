fruits = ["apple", "banana", "cherry"]

print("--- Fruit List ---")
print(fruits)

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Third fruit:", fruits[2])

fruits.append("orange")
fruits.append("grape")
print("Updated list:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

print("--- Looping through fruits ---")

for fruit in fruits[:]:
    fruits.remove(fruit)
print(fruits)