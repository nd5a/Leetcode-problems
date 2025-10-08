# Successful Pairs of Spells and Potions

import bisect
class Solution:
    def successfulPairs(self, spells, potions, success):
        P = len(potions)
        potions.sort()

        ans = []
        for s in spells:
            index = bisect.bisect_left(potions, True, key = lambda p: p * s >= success)
            ans.append(P -index)
        return ans