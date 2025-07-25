# Maximum Unique Subarray Sum After Deletion

class Solution:
    def maxSum(self, nums):
        s = list(set(x for x in nums if x  > 0))
        if len(s) == 0:
            return max(nums)
        return sum(s)