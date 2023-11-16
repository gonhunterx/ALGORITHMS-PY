nums = [1, 4, 3, 2, 4]
target = 7

i = 0
j = 1

for num in nums:
    if i + j == target:
        value = i + j
        print("1")
    else:
        i += 1
        j += 1
        if i + j == target:
            value = i + j
            print("2")
print(value)


# def is_there_a_zero(nums1):
# for i in nums1:
#     print(i, end=", ")

# length = len(nums1)
# for a in range(length):
#     if a == nums1[6]:
#         nums1.remove(a)
#     print(a)

# for num in nums1:
#     print(num)
#     if num == nums1[2]:
#         num_index_2 = num.remove()
#         print(num_index_2)


# nums1.append(nums2)
