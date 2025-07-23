# Maximum Score from removing substrings

class Solution:
    def maximumGain(self, s, x, y):
        first = [x, "ab"]
        second = [y, "ba"]

        if x < y:
            first, second = second, first
        
        total = 0
        for p, ss in [first, second]:
            stack = []
            for c in s:
                stack.append(c)

                if len(stack) >= 2 and stack[-1] == ss[1] and stack[-2] == ss[0]:
                    stack.pop()
                    stack.pop()
                    total += p
            s = "".join(stack)
        return total