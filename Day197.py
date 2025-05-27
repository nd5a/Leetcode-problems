# Divisible and Non-divisible sums difference

class Solution:
    def differenceOfSums(self, n, m):
        num1 = []
        num2 = []
        sum1 = 0
        sum2 = 0
        for i in range(1, n+1):
            if i % m != 0:
                num1.append(i)
                sum1 += i
            else:
                num1.append(i)
                sum2 += i
        return sum1-sum2
            