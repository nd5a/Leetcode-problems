# Longest Subarray of 1's After deleting One Element

class Solution:
    def longestSubarray(self, nums):
        N = len(nums)
        best = 0

        zero = 0
        left = 0

        for right in range(N):
            if nums[right] == 0:
                zero += 1
            
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            best = max(best, right - left + 1 - 1)
        return best
