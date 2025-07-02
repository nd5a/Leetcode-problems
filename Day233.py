# Find the Original Typed String II
from itertools import groupby
from functools import cache
import sys

sys.setrecursionlimit(10 ** 8)
fmax = lambda x, y: x if x > y else y
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(word)

        r = []
        for g, t in groupby(word):
            s = len(list(t))

            if s > 1:
                r.append(s - 1)
            k -= 1
        k= fmax(k, 0)

        @cache
        def f(index, left):
            if left == 0:
                return calculate(index, left)
            return calculate(index, left) + f(index, left - 1)
        
        @cache
        def calculate(index, left):
            if index == len(r):
                if left == 0:
                    return 1
                return 0
            
            total = 0
            total += f(index + 1, left)
            if left - r[index] - 1 >=0:
                total -= f(index + 1, fmax(left - r[index] - 1, 0))
            else:
                total += (r[index] - left) * f(index + 1, 0)
            
            return total % MOD
        
        r = calculate(0 , k) % MOD
        calculate.cache_clear()
        f.cache_clear()
        return r