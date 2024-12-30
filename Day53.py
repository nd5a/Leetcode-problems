# Count Ways to build good strings

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7

        def count(left):
            if left < 0:
                return 0
            if left == 0:
                return 1

            total = 0
            total += count(left - zero)

            total += count(left - one)

            return total % MOD

        total = 0
        for x in range(low, high + 1):
            total += count(x)
        return total % MOD
