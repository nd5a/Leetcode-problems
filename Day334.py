# Find Resultant Array After Removing Anagrams

import collections
class Solution:
    def removeAnagrams(self, words):
        ans = []

        def is_anagram(a, b):
            return collections.Counter(a) == collections.Counter(b)
        
        for word in words:
            if len(ans) == 0:
                ans.append(word)
                continue
            
            if not is_anagram(ans[-1], word):
                ans.append(word)
        return ans