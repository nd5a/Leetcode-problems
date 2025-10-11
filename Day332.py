# Maximum Total Damage with Spell Casting

from functools import cache
import collections
class Solution:
    def maximumTotalDamage(self, power):
        f = collections.Counter(power)

        keys = list(sorted(f.keys()))
        N = len(keys)

        @cache
        def get_max(index):
            if index >= N:
                return 0 
            
            best = get_max(index + 1)

            for i in range(1, 4):
                if index + i< N and keys[index + i] > keys[index] + 2:
                    best = max(best, get_max(index + i) + keys[index] * f[keys[index]])

            best = max(best, keys[index] * f[keys[index]])
            return best
        return get_max(0)