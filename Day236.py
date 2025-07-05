# Find Lucky Integer in an Array

import collections
class Solution:
    def findLucky(self, arr):
        f = collections.Counter(arr)

        best = -1
        for k in f.keys():
            if f[k] == k:
                best = max(best, k)
        return best