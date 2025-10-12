# Find Sum of array product of magical Sequences

from functools import cache

MOD = 10 ** 9 + 7
MAX = 55
fact = [1]
ifact = [1]

for i in range(1, MAX):
    fact.append((fact[-1] * i) % MOD)
    ifact.append(pow(fact[-1], -1, MOD))

class Solution:
    def magicalSum(self, m, k, nums):
        N = len(nums)

        @cache
        def f(index, mleft, kleft, carry):
            if index == N:
                if kleft == 0 and mleft == 0 and carry == 0:
                    return 1
                if carry.bit_count() == kleft and mleft == 0:
                    return 1
                return 0
            
            total = 0

            for i in range(mleft + 1):
                if  kleft >= (i + carry) % 2:
                    total += f(index + 1, mleft - i, kleft - ((i + carry) % 2), (carry + i) // 2) * pow(nums[index], i, MOD) * ifact[i]
            return total
        
        r = f(0, m, k, 0)
        f.cache_clear()
        return (r * fact[m]) % MOD