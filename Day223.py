# Divide a String into Group of size k

class Solution:
    def divideString(self, s, k, fill):
        N= len(s)
        ans = []
        for i in range(0, N, k):
            ans.append(s[i: i + k])

        if len(ans[-1]) < k:
            ans[-1] += fill * (k - len(ans[-1]))
        return ans