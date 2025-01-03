# Number of ways to split Array
class Solution:
    def waysToSplitArray(self, nums):
        N = len(nums)

        sum_left = 0
        sum_right = sum(nums)

        count = 0
        for i in range(N - 1):
            sum_left += nums[i]
            sum_right -= nums[i]

            if sum_left >= sum_right:
                count += 1
        return count