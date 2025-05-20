# Zero Array Transformation I

class Solution:
    def isZeroArray(self, nums, queries):
        N = len(nums)
        delta = [0] * (N + 1)
        for l, r in queries:
            delta[l] += 1
            delta[r + 1] -= 1
        
        for i in range(1, N + 1):
            delta[i] += delta[i - 1]
        
        for i in range(N):
            if nums[i] > delta[i]:
                return False
        return True