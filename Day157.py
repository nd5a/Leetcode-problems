# Count Equal and Divisible Pairs in an array

class Solution:
    def countPairs(self, nums, k):
        N = len(nums)
        count = 0

        for i in range(N):
            for j in range(i + 1, N):
                if i * j % k == 0 and nums[i] == nums[j]:
                    count += 1
        return count