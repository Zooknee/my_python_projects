nums_tuple = (10, 20, 30, 40, 50)
nums_list = [5, 15, 25]

# Convert tuple to list
nums_tuple_list = list(nums_tuple)

# Append all items from nums_list
nums_tuple_list.extend(nums_list)

# Remove 20
nums_tuple_list.remove(20)

# Reverse the list
nums_tuple_list.reverse()

# Print first 5 elements
print(nums_tuple_list[:5])

# Convert back to tuple
nums_tuple = tuple(nums_tuple_list)
print(nums_tuple)


nums_tuple = (10, 20, 30, 40, 50)
nums_list = [5, 15, 25]

nums_tuple = nums_list
nums_list.append(5)
nums_list.append(15)
nums_list.append(25)
nums_list.remove(20)
nums_list.reverse()
print(nums_list[:5])
nums_list = nums_tuple
print(nums_tuple)
