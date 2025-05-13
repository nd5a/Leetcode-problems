# Total Characters in string After Transformations I

class Solution:
    def lengthAfterTransformations(self, s, t):
        MOD = 10 ** 9 + 7
        f=[0] * 26
        for c in s:
            f[ord(c) - ord('a')] += 1
        
        for _ in range(t):
            nf = [0] * 26
            for i in range(26):
                f[i] %= MOD
                nf[(i + 1) % 26] += f[i]
                if i== 25:
                    nf[1] += f[i]
            f = nf
        return sum(f) % MOD