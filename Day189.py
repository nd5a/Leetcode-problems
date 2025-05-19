# Types of Triangles

class Solution:
    def triangleType(self, nums):
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        distinct = len(set(nums))
        if distinct == 1:
            return "equilateral"
        if distinct == 2:
            return "isosceles"
        return "scalene"