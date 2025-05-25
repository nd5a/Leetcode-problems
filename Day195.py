# Longest Palindrome by Concatenating Two letter words

import collections
class Solution:
    def longestPalindrome(self, words):
        f = collections.Counter(words)

        total = 0
        extra = 0
        for k in f.keys():
            if k[0] == k[1]:
                if f[k] % 2 == 1:
                    extra = 1
                total += (f[k] // 2) * 4
            else:
                rk = k[1] + k[0]
                total += min(f[k], f[rk]) * 2
        return total + extra * 2