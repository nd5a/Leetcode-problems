# Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n):
        result = []
        
        # If n is even, add pairs like (-1,1), (-2,2), ..
        for i in range(1, n // 2 + 1):
            result.append(-i)
            result.append(i)
        
        # If n is odd, add 0 to balance
        if n % 2 == 1:
            result.append(0)
        
        return result
