# Convert All Integer to the Sum of Two No-Zero Integers

class Solution:
    def getNoZeroIntegers(self, N):
        for a in range(1, N):
            b = N - a

            if "0" not in str(a) and "0" not in str(b):
                return [a, b]
        assert(False)