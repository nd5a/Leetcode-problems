# Largest Perimeter Triangle

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)

        for c, b, a in zip(nums, nums[1:], nums[2:]):
            if a + b > c:
                return a + b + c
        else:
            return 0