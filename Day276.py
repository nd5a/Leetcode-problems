# Powers of Four

import math
class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        
        s = math.sqrt(n)
        if s != int(s):
            return False
        
        s = int(s)
        if (s & (s - 1)) == 0:
            return True
        return False