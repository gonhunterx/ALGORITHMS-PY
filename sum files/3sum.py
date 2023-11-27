# import numpy as np


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initalize an empty results list to append triplets to
        res = []
        # sort the values in the nums list
        nums.sort()
        # create a loop that will go through up till the third to last element because we do not want to go out of
        # index range so we use -2
        for i in range(len(nums) - 2):
            #
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
