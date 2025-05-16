# Longest Unequal Adjacent Group Subsequence II

class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        N = len(words)

        def is_ham_one(i, j):
            L = len(words[i])
            count = 0
            for k in range(L):
                if words[i][k] != words[j][k]:
                    count += 1
                if count > 1:
                    return False
            return count == 1
        
        dp = [1] * N
        prev = [-1] * N
        for i in range(N):
            for j in range(i + 1, N):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and is_ham_one(i, j):
                    if dp[j] < dp[i] + 1:
                        dp[j] = dp[i] +1
                        prev[j] = i
        besti = 0
        for i in range(1, N):
            if dp[i] > dp[besti]:
                besti = i
        ans = []

        current = besti
        while current != -1:
            ans.append(words[current])
            current = prev[current]
        ans.reverse()
        return ans