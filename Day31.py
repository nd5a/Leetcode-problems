# Maximum number of integers to Choose from a range

class Solution:
    def maxCount(self, banned, n, maxSum):
        b = set(banned)

        count = 0
        total = 0

        for i in range(1, n + 1):
            if i in b:
                continue
            
            if total + i <= maxSum:
                count += 1
                total += i
            else:
                break
        
        return count