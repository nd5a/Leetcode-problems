# Find Words Containing a Character


class Solution:
    def findWordsContaining(self, words, x):
        ans = []
        for index, word in enumerate(words):
            if x in word:
                ans.append(index)
        return ans