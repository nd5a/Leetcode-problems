# Count the Numeber of Arrays with K matching Adjacent Elements

MAX = 1000005
class Solution:
    def countGoodArrays(self, n, m, k):
        MOD = 10 ** 9 + 7

        fact = [1]
        ifact = [1]
        for i in range(1, n):
            fact.append((fact[-1] * i) % MOD)
            ifact.append(pow(fact[-1], -1, MOD))
        return (m * pow(m - 1, n - 1 - k, MOD) * fact[n-1] * ifact[k] * ifact[n - 1 - k]) % MOD