# Number of Sub - arrays with Odd sum

class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10 ** 9 + 7

        total = 0
        prev_zero = 0
        prev_one = 0

        prev_zero += 1

        p = 0
        for x in arr:
            p += x
            p %= 2

            if  p == 0:
                total += prev_one
            else:
                total += prev_zero
            
            if p == 0:
                prev_zero += 1
            else:
                prev_one += 1
        return total % MOD
