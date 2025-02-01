# Special Array I

import itertools

class Solution:
    def isArraySpecial(self, nums):
        N = len(nums)

        for x, y in itertools.pairwise(nums):
            if (x % 2) == (y % 2):
                return False
        return True