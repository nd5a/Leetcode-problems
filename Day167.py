# Count subarrays of length three with a condition

class Solution:
    def countSubarrays(self, nums):
        N = len(nums)
        count = 0
        for i in range(N - 2):
            if 2 * (nums[i] + nums[i + 2]) == nums[i + 1]:
                count += 1
        return count