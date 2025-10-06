print("--- For Loop ---")
for i in range(11):
    print("Hello", i)

print("--- While Loop ---")
count = 0
while count <= 10:
    print("Hello", count)
    count = count + 1
print("--- Break Example ---")
for i in range(10):
    if i == 5:
        print("Stopping at", i)
        break
    print("Number:", i)

print("--- Continue Example ---")
for i in range(10):
    if i % 2 == 0:
         continue
    print("Odd number:", i)

print("--- Mini Challenge (While Loop) ---")

count = 1
while count <= 20:
    if count % 3 == 0:   # skip numbers divisible by 3
        count += 1
        continue
    if count == 17:      # stop loop completely
        break
    print(count)
    count += 1


print("--- Mini Challenge ---")

for i in range(1, 21):   # counts from 1 to 20
    if i % 3 == 0:       # skip numbers divisible by 3
        continue
    if i == 17:          # stop loop completely
        break
    print(i)
