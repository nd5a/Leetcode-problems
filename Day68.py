# Find the Prefix Comman Array of Two Arrays

import collections
from collections import Counter
class Solution:
    def findThePrefixCommonArray(self, A, B):
        N = len(A)
        ans = []
        count = 0
        f = collections.Counter()

        for a,b in zip(A, B):
            f[a] -= 1
            f[b] += 1

            if f[a] == 0:
                count += 1
            if f[b] == 0:
                count += 1
            if a == b:
                count -= 1
            
            ans.append(count)
        return ans