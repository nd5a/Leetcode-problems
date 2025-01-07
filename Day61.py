# Strings matching in an array

class Solution:
    def stringMatching(self, words):
        N = len(words)

        ans = []
        for i in range(N):
            good = False
            for j in range(N):
                if i != j and words[i] in words[j]:
                    good = True
                    break
            if good:
                ans.append(words[i])
        return ans