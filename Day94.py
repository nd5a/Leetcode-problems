# Count Number of Bad Pairs

import collections

class Solution:
    def countBadPairs(self, nums):
        N = len(nums)
        f = collections.Counter()
        total = 0
        for i in range(N):
            j = i
            total += j - f[nums[j] - j]
            f[nums[i] - i] += 1
        return total