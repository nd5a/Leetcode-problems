# Using a Robot to print the lexicographically smallest string

class Solution:
    def robotWithString(self, s):
        n = len(s)
        # next_min[i] = minimum character in s[i:]
        next_min = [''] * (n + 1)
        next_min[n] = '{'  # sentinel greater than 'z'
        for i in range(n - 1, -1, -1):
            next_min[i] = min(s[i], next_min[i + 1])

        stack = []
        result = []

        i = 0
        while i < n:
            stack.append(s[i])
            i += 1

            while stack and (i == n or stack[-1] <= next_min[i]):
                result.append(stack.pop())

        while stack:
            result.append(stack.pop())

        return ''.join(result)
