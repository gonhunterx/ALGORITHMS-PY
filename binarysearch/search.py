nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 4


def search(nums, target):
    left, right = 0, len(nums) - 1
    # not using <= to ensure that the left stays in bounds
    while left < right:
        mid = (left + right) // 2
        # check if the target is less than the right pointer
        if nums[mid] >= target:
            # if it is larget or equal then we set right to that index and continue
            right = mid
        else:
            left = mid + 1
    # making sure the left pointer is in bounds and checking if it equals the target
    if left < len(nums) and nums[left] == target:
        return left
    else:
        return -1


print(search(nums, target))
