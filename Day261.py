# Longest Subarray With Maximum Bitwise AND

class Solution:
    def longestSubarray(self, nums):
        mx = max(nums)

        streak = 0
        best = 0
        for x in nums:
            if x == mx:
                streak += 1
            else:
                streak = 0
            
            best = max(best, streak)
        return best