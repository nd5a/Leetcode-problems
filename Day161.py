# Count the Hidden Sequences

class Solution:
    def numberOfArrays(self, differences, lower, upper):
        current = 0
        hi = 0
        lo = 0
        for d in differences:
            current += d
            hi = max(hi, current)
            lo = min(lo, current)
        
        shift = (upper - hi)
        lo += shift

        return max(lo - lower + 1, 0)