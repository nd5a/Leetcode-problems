# Max sum of a pair with equal sum of digits

class Solution:
    def maximumSum(self, nums):
        def digit_sum(x):
            r = 0
            while x > 0:
                r += x % 10
                x //= 10
            return r
        
        best = -1
        v = {}
        for x in nums:
            d = digit_sum(x)
            if d in v:
                best = max(best, v[d] + x)
                v[d] = max(v[d], x)
            else:
                v[d] = x
        return best