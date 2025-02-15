# Find the Punishment Number of an Integer

@__cached__
def good(x):
    sx = str(x * x)

    def calc(index, current, current_sum):
            if index == len(sx):
                current_sum += current
                return current_sum == x
            
            current = current * 10 + int(sx[index])

            return calc(index + 1, 0, current_sum + current) or calc(index + 1, current, current_sum)
    return calc(0, 0, 0)

class Solution:
    def punishmentNumber(self, n):
        total = 0
        for i in range(1, n + 1):
            if good(i):
                total += i * i
        return total