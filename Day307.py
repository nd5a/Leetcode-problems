# Replace Non-Coprime Numbers in Array

from math import lcm, gcd
class Solution:
    def replaceNonCoprimes(self, nums):
        N = len(nums)
        stack =[]

        for x in nums:
            stack.append(x)

            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()

                l = lcm(a,b)
                stack.append(l)
        return stack
