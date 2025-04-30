# Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums):
        count = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                count += 1
        return count