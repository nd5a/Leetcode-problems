# Check if Number is a Sum of Power of Three

class Solution:
    def checkPowersOfThree(self, D: int) -> bool:
        while D > 0:
            digit = D % 3
            D // 3

            if digit == 2:
                return False
        return True