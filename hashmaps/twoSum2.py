nums = [1, 2, 5, 4, 2]
target = 3


def twoSum(nums, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            # since we already know the diff we just return
            print([prevMap[diff], i])
            return [prevMap[diff], i]
        # here we are adding the value to the hashmap
        # n is the key value and i is the index
        prevMap[n] = i
    return


twoSum(nums, target)
