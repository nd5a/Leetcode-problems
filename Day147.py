# Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums):
        N = len(nums)

        total = sum(nums)

        if total % 2 == 1:
            return False
        
        dp = set([0])
        for x in nums:
            ndp = set()
            for y in dp:
                ndp.add(y)
                ndp.add(y + x)
            dp = ndp
        
        return (total // 2) in dp