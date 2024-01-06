import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # make sure no smaller vals exist 
            while q and nums[q[-1]] < nums[r]:
                # pop smaller vals
                q.pop()
            
            # appending the indexes 
            q.append(r)
            
            # remove left val from window if out of bounds 
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output