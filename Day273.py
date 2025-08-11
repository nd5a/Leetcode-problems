# Range Product Queries of Powers

class Solution:
    def productQueries(self, N: int, queries):
        MOD = 10 ** 9 + 7

        r = []
        for i in range(32):
            if (N & (1 << i)) > 0:
                r.append(1 << i)
        
        ans = []
        for s, e in queries:
            j = 1
            for i in range(s, e + 1):
                j *= r[i]
                j %= MOD
            ans.append(j)
        return ans