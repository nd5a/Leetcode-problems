# Minimum Operations to Make Array Values Equal to K

class Solution:
    def minOperations(self, nums, k):
        if any(x < k for x in nums):
            return -1
        return len(set(x for x in nums if x >k))