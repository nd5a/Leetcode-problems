# Paintings Grid with Three Different Colors

from functools import cache

class Solution:
    def colorTheGrid(self, R, C):
        MOD = 10 ** 9 + 7
        @cache
        def count(mask, x, y):
            if x == R:
                return count(mask, 0, y + 1)
            if y == C:
                return 1
            
            total =0 

            if x - 1 >= 0:
                colour_above = (mask % 3)
            else:
                colour_above = -1
            
            if y - 1 >= 0:
                colour_left = mask//(3 ** (R- 1))
            else:
                colour_left = -1
            
            for c in range(3):
                if c != colour_above and c != colour_left:
                    new_mask = (mask * 3 + c) % (3 ** R)
                    total += count(new_mask, x + 1, y)
            return total % MOD
        return count(0, 0 , 0) % MOD