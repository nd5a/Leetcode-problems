# Numbers of Zero-Filled SubarrayS

class Solution:
    def zeroFilledSubarray(self, nums):
        N = len(nums)

        streak = 0
        total = 0

        for x in nums:
            if x == 0:
                streak += 1
                total += streak
            else:
                streak = 0
        return total