# Find Traingular Sum of an Array

class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        current = nums[:]

        while len(current) > 1:
            nxt = []

            for x, y in zip(current, current[1:]):
                nxt.append((x + y) % 10)
            current = nxt
        return current[0]