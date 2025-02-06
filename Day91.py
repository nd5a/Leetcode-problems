# Tuple with Same product

import collections

class Solution:
    def tupleSameProduct(self, nums):
        N = len(nums)

        f = collections.Counter()
        for i in range(N):
            for j in range(i + 1, N):
                f[nums[i] * nums[j]] += 1
        
        total = 0
        for key in f.keys():
            total += f[key] * (f[key] - 1) * 4
        return total