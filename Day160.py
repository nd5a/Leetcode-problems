# Rabbits in Forest

import collections

class Solution:
    def numRabbits(self, answers):
        f = collections.Counter(answers)

        total = 0
        for k in f.keys():
            total += ((f[k] + k) // (k + 1)) * (k + 1)
        return total 