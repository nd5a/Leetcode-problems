# Check If a Parentheses String Can be Valid

class Solution:
    def canBeValid(self, s, locked):
        def is_valid(left, right, s, locked):
            N = len(s)
            depth = 0
            unused = 0
            for i in range(N):
                if locked[i] == "1":
                    if s[i] == left:
                        depth += 1
                    else:
                        depth -= 1

                        if depth < 0:
                            if unused > 0:
                                unused -= 1
                                depth += 1
                            else:
                                return False
                else:
                    unused += 1
            return (unused - depth) % 2 == 0
        return is_valid("(", ")", s, locked) and is_valid(")", "(", s[::-1], locked[::-1])