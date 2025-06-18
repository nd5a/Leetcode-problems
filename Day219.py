# Divide Array into Arrays with max Difference

class Solution:
    def divideArray(self, nums, k):
        N = len(nums)
        nums.sort()

        ans = []
        for i in range(0, N, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i:i+3])
        return ans