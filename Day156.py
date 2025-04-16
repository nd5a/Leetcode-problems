# Count the Number of Good Subarrays

import collections
class Solution:
    def countGood(self, nums, k):
        N = len(nums)

        #seen is the number of each element inside the window

        seen = collections.Counter()
        pairs = 0
        total = 0
        left = 0
        for right in range(N):
            pairs += seen[nums[right]]
            seen[nums[right]] += 1

            while pairs >= k:
                seen[nums[left]] -=1 
                pairs -= seen[nums[left]]
                left += 1
            total += left
        return total