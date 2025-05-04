# Number of Equivalent Domino Pairs

import collections
class Solution:
    def numEquivDominoPairs(self, dominoes):
        total = 0
        lookup = collections.Counter()
        for x, y in dominoes:
            if x > y:
                x, y = y, x
            total += lookup[(x, y)]
            lookup[(x, y)] += 1
        return total