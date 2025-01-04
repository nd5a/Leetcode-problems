# Unique Length-3 Palindromic Subsequences

import collections
class Solution:
    def countPalindromicSubsequence(self, s):
        N = len(s)

        left = collections.Counter()
        left_mask = 0
        right = collections.Counter(s)
        right_mask = 0
        
        for c in right.keys():
            right_mask |= 1 << (ord(c) - ord('a'))

        middle_mask = [0] * 26
        for i in range(N):
            if i >= 1:
                left[s[i - 1]] += 1
                left_mask |= 1<< (ord(s[i - 1]) - ord('a'))
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right_mask ^= 1 << (ord(s[i]) - ord('a'))
            
            middle_mask[ord(s[i]) - ord('a')] |= (left_mask & right_mask)
        
        total = 0
        for x in middle_mask:
            total += x.bit_count()
        return total