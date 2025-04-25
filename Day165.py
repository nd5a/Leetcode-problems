# Count of Interesting Subarrays

import collections
class Solution:
    def countInterestingSubarrays(self, nums, modulo, k):
        N = len(nums)

        prev = collections.Counter()
        prev[0] = 1
        total = 0
        current = 0
        degree = 1

        for i in range(N):
            if nums[i] % modulo == k:
                current += 1
            total += prev[(current - k) % modulo]
            prev[current % modulo] += 1
        return total