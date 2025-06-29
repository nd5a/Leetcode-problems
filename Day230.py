# Number of Subsequences That Satisfy the Given Sum Condition

class Solution:
    def numSubseq(self, nums, target):
        nums.sort()
        res = 0
        mod = (10 ** 9 + 7)

        r = len(nums) - 1
        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            if i <= r:
                res += (2 ** (r - i))
                res %= mod
        return res