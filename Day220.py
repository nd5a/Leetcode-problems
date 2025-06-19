# Partition Array such that Maximum Difference Is K

class Solution:
    def partitionArray(self, nums, k):
        INF = 10 ** 20
        nums.sort()

        count = 0
        start = -INF
        for x in nums:
            if x - start > k:
                count +=1
                start = x
        return count