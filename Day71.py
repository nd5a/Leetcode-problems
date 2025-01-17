# Neighboring Bitwise XOR

class Solution:
    def doesValidArrayExist(self, derived):
        x = 0
        for c in derived:
            x ^= c
        return x == 0