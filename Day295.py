# Find Closest Person

class Solution:
    def findClosest(self, x, y, z):
        d = abs(x - z) - abs(y - z)
        if d > 0:
            return 2
        elif d < 0:
            return 1
        return 0