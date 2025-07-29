# Smallest Subarrays with maximum bitwise OR

class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        last_seen = [-1] * 32  # store the last position for each bit
        ans = [1] * n  # by default, every subarray has at least length 1

        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    last_seen[bit] = i  

            max_end = i
            for j in range(32):
                if last_seen[j] != -1:
                    max_end = max(max_end, last_seen[j])

            ans[i] = max_end - i + 1 
        return ans
