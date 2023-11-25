my_dict = {}

nums = [88, 22, 342, 22, 44, 12, 12]

result = []

for index, num in enumerate(nums):
    key = index
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(num)
print(my_dict)

for key, value in my_dict.items():
    for element in value:
        if element >= 50:
            result.append(element)
        else:
            continue

print(result)
