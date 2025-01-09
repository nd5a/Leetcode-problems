# Counting words with a Given prefix

class Solution:
    def prefixCount(self, words, pref):
        count = 0 
        for word in words:
            if word.startswith(pref):
                count += 1
        return count