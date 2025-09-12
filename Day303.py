# Vowels Game in String

class Solution:
    def doesAliceWin(self, s):
        for c in "aeiou":
            if c in s:
                return True
        else:
            return False