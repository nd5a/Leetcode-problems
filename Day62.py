# Count Prefix and Suffix Pairs I

class Solution:
    def countPrefixSuffixPairs(self, words):
        N = len(words)

        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)

        count = 0
        for i in range(N):
            for j in range(i + 1, N):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count