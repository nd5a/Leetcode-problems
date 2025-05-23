# Find the Maximum Sum of node values

class Solution:
    def maximumValueSum(self, nums, k, edges):
        N = len(nums)

        delta = []
        for x in nums:
            delta.append((x ^ k) - x)
        delta.sort(reverse = True)

        total=  sum(nums)
        for i in range(0, N, 2):
            if i + 1>= N:
                continue
            a, b = delta[i], delta[i + 1]
            if a + b > 0:
                total += (a + b)
        return total