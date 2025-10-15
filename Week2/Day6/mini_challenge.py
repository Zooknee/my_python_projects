# my version
for i in range(1, 21):
    if i % 3:
        continue
    else:
        i >= 15
    print("Number is:", i)
    
#correct version
for i in range(1, 21):
    if i % 3 != 0:   # skip numbers NOT divisible by 3
        continue
    if i >= 15:      # stop the loop once we hit 15 or higher
        break
    print("Number is:", i)

