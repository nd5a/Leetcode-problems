# Find the number of distinct colors among the balls

import collections

class Solution:
    def queryResults(self, limit, queries):
        N = limit + 1
        f = collections.Counter()
        colours = collections.defaultdict(lambda: 0)
        ccount = 0

        ans = []
        for x, y in queries:
            prev = colours[x]
            if prev != 0:
                f[prev] -= 1
                if f[prev] == 0:
                    ccount -= 1
            
            colours[x] = y
            f[y] += 1
            if f[y] == 1:
                ccount += 1
            ans.append(ccount)
        return ans