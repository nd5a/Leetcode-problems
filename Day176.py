# Build Array from Permutation

class Solution:
    def buildArray(self, nums):
        N = len(nums)
        ans = [0] * N
        for i in range(N):
            ans[i] = nums[nums[i]]
        return ans
        