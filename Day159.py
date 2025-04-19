# Count the Number of Fair Pairs

import bisect

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        # give the number of nubers that satisfies nums[j] <= x AND j >= start
        def f(start, x):
            return bisect.bisect_right(nums, x, lo = start)

        total = 0
        for i,x in enumerate(nums):
            total += f(i + 1, upper- x) - f(i + 1, lower - 1 - x)
        return total
