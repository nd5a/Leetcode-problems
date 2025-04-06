# Largest Divisible Subset

class Solution:
    def largestDivisibleSubset(self, nums):
        N = len(nums)
        nums.sort()

        dp = [1] * N
        prev = [None] * N

        for i in range(1, N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        
        best = max(dp)
        for i in range(N -1, -1, -1):
            if dp[i] == best:
                ans = []
                current = i
                while prev[current] is not None:
                    ans.append(nums[current])
                    current = prev[current]
                
                ans.append(nums[current])
                return ans
        else:
            assert(False)