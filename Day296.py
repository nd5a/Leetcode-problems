# Minimum Operations to Make the Integer zero

class Solution:
    def makeTheIntegerZero(self, num1, num2):
        if num1 == 0:
            return 0
        for k in range(60):
            now = num1 - (num2 * k)

            if now >= k and now.bit_count() <= k:
                return k
        else:
            return -1
            