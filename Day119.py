# Find Missing and Repeated Values

import collections

class Solution:
    def findMissingAndRepeatedValues(self, grid):
        N = len(grid)
        total = collections.Counter()
        for row in grid:
            total += collections.Counter(row)
        
        s = 0
        ans = [None, None]
        for k, v in total.items():
            s += k * v
            if v== 2:
                ans[0] =k
        s -=ans[0]

        M = N *N
        b = M*(M + 1) // 2 - s
        ans[1] = b
        return ans