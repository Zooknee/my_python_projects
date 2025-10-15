# Basic Set Operations
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)

fruits.add("orange")
print("After adding:", fruits)

fruits.remove("banana")
print("After removing:", fruits)

# Set math
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))
