# Smallest Missing Non-negative Integer After Operations

import collections
class Solution:
    def findSmallestInteger(self, nums, value):
        N = len(nums)

        d = collections.Counter()

        for i in range(N):
            nums[i] %= value
            d[nums[i]] += 1
        
        i = 0
        while d[(i % value)] > 0:
            d[i % value] -= 1
            i += 1
        return i