# Minimum Operation to Make Array Elements Zero

import math

class Solution:
    def minOperations(self, queries):
        def steps_sum(l, r):
            """Return total steps required to make all numbers in [l, r] zero."""
            total = 0
            k = 1
            start = 1
            while start <= r:
                end = 4 ** k - 1
                left = max(l, start)
                right = min(r, end)
                if left <= right:
                    total += (right - left + 1) * k
                k += 1
                start *= 4
            return total
        
        ans = 0
        for l, r in queries:
            total_steps = steps_sum(l, r)
            ans += (total_steps + 1) // 2   # ceil division
        return ans
