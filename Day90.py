# Check if One String swap can make string equal
import collections

class Solution:
    def areAlmostEqual(self, s1, s2):
        f1 = collections.Counter(s1)
        f2 = collections.Counter(s2)

        if f1 != f2:
            return False
        
        N = len(s1)
        count = 0
        for i in range(N):
            if s1[i] != s2[i]:
                count += 1
        return count == 0 or count == 2