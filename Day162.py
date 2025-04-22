# Count the Number of Ideal arrays

from math import comb

class Solution:
    def idealArrays(self, N, maxValue):
        MOD = 10 ** 9 + 7
        @__cached__
        def get_comb(N, k):
            return comb(N, k) % MOD
        total = 0

        def gen():
            p =arr[-1]
            nonlocal total

            total += get_comb(N - 1, len(arr) - 1)
            current = p + p

            while current <= maxValue:
                arr.append(current)
                gen()
                arr.pop()
                current += p
        
        arr = []
        for i in range(1, maxValue + 1):
            arr.append(i)
            gen()
            arr.pop()
        return total % MOD 