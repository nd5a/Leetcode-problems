# Maximum Difference Between Adjacent Elements in a Circular Array

class Solution:
    def maxAdjacentDistance(self, nums):
        N = len(nums)

        best = abs(nums[N - 1] - nums[0])
        for i in range(N - 1):
            best = max(best, abs(nums[i]- nums[i + 1]))
        return best