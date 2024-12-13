# Make String a Subsequence using cyclic Increments

class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        N = len(str1)
        M = len(str2)
        def f(c):
            return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
        i = 0
        for j in range(M):
            while i < N and (str1[i] != str2[j] and f(str1[i]) != str2[j] ):
                i += 1
            if i >= N:
                return False
            
            i += 1
        else:
            return True