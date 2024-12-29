# Number of Ways form a Target string Given a Dictionary

import collections

class Solution:
    def numWays(self, words, target):
        MOD = 10 ** 9 + 7
        N = len(words)
        L = len(words[0])
        T = len(target)

        def get_count(windex):
            f = collections.Counter()
            for i in range(N):
                f[words[i][windex]] += 1
            return f

        def count(windex, tindex):
            if tindex == T:
                return 1
            if windex == L:
                return 0
            
            total = 0

          
            total += get_count(windex) [target[tindex]] * count(windex + 1, tindex + 1)
            total %= MOD
            
            total += count(windex + 1, tindex)
            total %= MOD
            return total
        
        return count(0, 0) % MOD