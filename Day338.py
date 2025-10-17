# Maximize the Number of Partitions After Operations

from functools import cache
class Solution:
    def maxPartitionsAfterOperations(self, s, k):
        N = len(s)
        @cache

        def f(index, used, seen):
            if index >= N:
                return 0 
            best = 0
        
            c = ord(s[index]) - ord('a')
            nseen = seen | (1 << c)

            if nseen.bit_count() > k:
                best = max(best, 1 + f(index + 1, used, 1 << c))
            else:
                best = max(best, f(index + 1, used, nseen))
            
            if not used:
                for c in range(26):
                    nseen = seen | (1 << c)
                    if nseen.bit_count() > k:
                        best = max(best, 1 + f(index + 1, True, (1 << c)))
                    else:
                        best = max(best, f(index + 1, True, nseen))
            return best

        return f(0, False, 0) + 1