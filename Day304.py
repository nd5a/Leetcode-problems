# Find Most Frequent Vowel and Consonant

import collections
class Solution:
    def maxFreqSum(self, s: str) -> int:
        f = collections.Counter(s)

        vowels = cons = 0
        for k, v in f.items():
            if k in "aeiou":
                vowels = max(vowels, v)
            else:
                cons = max(cons, v)
        return vowels + cons