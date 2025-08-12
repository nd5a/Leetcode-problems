# Ways to Express an Integer as Sum of Powers

class Solution:
    def numberOfWays(self, N, x):
        MOD = 10 ** 9 + 7

        ways = [0] * (N + 1)
        ways[0] = 1

        for i in range(1, int(pow(N, 1 / x)) + 2):
            c = pow(i, x)

            for j in range(N, -1, -1):
                if j - c >= 0:
                    ways[j] += ways[j - c]
                    ways[j] %= MOD
        return ways[N] % MOD