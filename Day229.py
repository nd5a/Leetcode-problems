# Find Subsequence of Length K with the Laegest Sum

class Solution:
    def maxSubsequence(self, nums, k):
        s = list(sorted(enumerate(nums), key = lambda x : (-x[1], x[0])))

        return list(x for _, x in sorted(s[:k], key = lambda x : x[0]))