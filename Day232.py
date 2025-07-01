# Find the Original Typed String I

class Solution:
    def possibleStringCount(self, word):
        total = 0

        streak = 0
        current = ""

        for c in word:
            if c == current:
                streak += 1
                total += 1
            else:
                current = c
                streak = 1
        return total + 1