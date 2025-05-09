# Count Number of Balanced Permutations

from functools import cache
from math import factorial
import collections
class Solution:
    def countBalancedPermutations(self, num):
        N = len(num)
        arr = sorted([int(x) for x in num])
        f = collections.Counter(arr)
        MOD = 10 ** 9 + 7

        even = N //2
        odd = N - even
        total_factorial = factorial(odd) * factorial(even)

        @cache
        def count(current, delta, odd_left, even_left):
            if current == 10:
                if delta == 0 and odd_left == 0 and even_left == 0:
                    return total_factorial
                return 0
            total = 0
            for i in range(f[current] + 1):
                if odd_left >= i and even_left >=   f[current] - i:
                    t= count(current + 1, delta+i * current - (f[current] - i)* current, odd_left - i, even_left - (f[current] - i))
                    if t == 0:
                        continue
                    
                    t//= factorial(i) * factorial(f[current] - i)
                    total += t
            return total
        return (count(0, 0, odd, even) % MOD)
