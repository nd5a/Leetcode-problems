# Minimum Operations to Make Binary Array Elements Equal to One I

class Solution:
    def minOperations(self, nums):
        N = len(nums)
        count = 0
        for i in range(2, N):
            if nums[i -2] == 0:
                nums[i-2] = 1 - nums[i -2]
                nums[i-1] = 1 - nums[i -1]
                nums[i] = 1-nums[i]
                count += 1
        if nums[N - 2] == 0 or nums[N-1] == 0:
            return -1
        return count