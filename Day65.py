# Construct K Palindrome Strings

from collections import Counter
import collections
class Solution:
    def canConstruct(self, s, k):
        f = collections.Counter(s)

        if k > len(s):
            return False
        
        odd = 0
        for c in f.keys():
            if f[c] % 2 == 1:
                odd += 1
        
        if odd > k:
            return False
        return True