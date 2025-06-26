# Longest Binary Subsequence Less Than or Equal to K

class Solution:
    def longestSubsequence(self, s, k):
        N = len(s)

        best = 0
        current = 0
        current_digits = 0

        for i in range(N - 1, -1, -1):
            x = int(s[i])

            if x == 0:
                current_digits += 1
            else:
                if current_digits >= 40:
                    continue
                
                if current + pow(2, current_digits) <= k:
                    current += pow(2, current_digits)
                    current_digits += 1
            best = max(best, current_digits)
        return best