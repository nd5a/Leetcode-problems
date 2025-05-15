# Longest Unequal Adjacent Group Subsequence I

class Solution:
    def getLongestSubsequence(self, words, groups):
        N = len(words)
        last = groups[0]
        ans = [words[0]]

        for i in range(1, N):
            if groups[i] != last:
                last = groups[i]
                ans.append(words[i])
        return ans