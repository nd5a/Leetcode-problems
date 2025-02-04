# Maximum Ascending Subarray Sum

class Solution:
    def maxAscendingSum(self, nums):
        N = len(nums)

        current_sum = nums[0]
        best = current_sum

        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i] 
            else:
                current_sum = nums[i]
            best = max(best, current_sum)
        return best