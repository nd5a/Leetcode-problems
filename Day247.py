# Find the Maximum Length of Valid Subsequence I

class Solution:
    def maximumLength(self, nums):
        n = len(nums)

        countEven = 0
        countOdd = 0
        alternating = 1
        for i in nums:
            if i % 2 == 0:
                countEven += 1
            else:
                countOdd += 1
        
        parity = nums[0] % 2

        for i in range(n):
            currParity = nums[i] % 2
            if currParity != parity:
                alternating += 1
                parity = currParity
        
        return max(countEven, countOdd, alternating)
