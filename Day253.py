# Maximum Erasure Value

import collections
class Solution:
    def maximumUniqueSubarray(self, nums):
        N = len(nums)

        # the frequency table of things inside the "window"
        f = collections.Counter()

        # total is the sum inside the window
        total = 0
        left = 0
        best = 0
        for right in range(N):
            f[nums[right]] += 1
            total += nums[right]

            while f[nums[right]] > 1:
                f[nums[left]] -= 1
                total -= nums[left]
                left += 1
            best = max(best, total)
        return best