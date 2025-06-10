# Maximum Difference Between Even and Odd Frequency I

import collections
class Solution:
    def maxDifference(self, s):
        f = collections.Counter(s)

        INF = 1000
        odd_max = 0
        even_min = INF

        for v in f.values():
            if v % 2 == 0:
                even_min = min(even_min, v)
            else:
                odd_max = max(odd_max, v)
        return odd_max - even_min