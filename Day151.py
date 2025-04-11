# Count Symmetric Integers

class Solution:
    def countSymmetricIntegers(self, low, high):
        def good(x):
            xs = str(x)
            if len(xs) % 2 == 1:
                return False
            first = 0
            for i in xs[:len(xs) // 2]:
                first += int(i)
            second = 0
            for i in xs[len(xs) // 2:]:
                second += int(i)
            return first == second
        count = 0
        for x in range(low, high + 1):
            if good(x):
                count += 1
        return count