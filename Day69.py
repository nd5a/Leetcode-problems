# Minimize XOR

class Solution:
    def minimizeXor(self, num1, num2):
        B = num2.bit_count()
        M = 31
        x = 0
        for i in range(M, -1, -1):
            if (num1 & (1 << i)) > 0:
                if B > 0:
                    B -= 1
                    x |= (1 << i)
            else:
                if B >= (i + 1):
                    B -= 1
                    x |= (1 << i)
        return x
