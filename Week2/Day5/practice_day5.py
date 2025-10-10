nums_list = [1, 2, 3, 4, 5]
nums_tuple = (10, 20, 30)
nums_set = {3, 4, 5, 6}
info = {"name": "Isaiah", "role": "student"}

nums_list.append(6)
nums_list[1] = 99

tmp = list(nums_tuple)
tmp.extend([40, 50])
nums_tuple = tuple(tmp)

nums_set.add(7)
nums_set.discard(3)

info["list_len"] = len(nums_list)
info["tuple_sum"] = sum(nums_tuple)

print("nums_list:", nums_list)
print("nums_tuple:", nums_tuple)
print("nums_set:", nums_set)
print("info:", info)

