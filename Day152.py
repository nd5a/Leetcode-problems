# Find the Count of Good Integers
import math
import collections

class Solution:
    def countGoodIntegers(self, N, k):
        if N == 1:
            count = 0
            for i in range(1, 10):
                if i % k == 0:
                    count += 1
            return count
        
        n = N // 2
        count = 0
        s = set()
        if N % 2 == 0:
            for i in range(pow(10, n-1), pow(10, n)):
                if int(str(i) + str(i)[::-1]) % k == 0:
                    key = "".join(sorted(list(str(i) + str(i)[::-1])))
                    s.add(key)
                    count += 1
        else:
            for i in range(pow(10, n - 1), pow(10, n)):
                for m in range(10):
                    if int(str(i) + str(m) + str(i)[::-1]) % k == 0:
                        key = "".join(sorted(list(str(i) + str(m) + str(i)[::-1])))
                        s.add(key)
                        count += 1
        total = 0
        factN = math.factorial(N)
        factN1 = math.factorial(N -1)
        for x in s:
            current = factN
            f = collections.Counter(x)

            for _, v in f.items():
                current //= math.factorial(v)
            
            if f["0"]>0:
                zero_current = factN1
                for k, v in f.items():
                    if k == "0":
                        zero_current //= math.factorial(v-1)
                    else:
                        zero_current //= math.factorial(v)
                
                current -= zero_current
            total += current
        return total