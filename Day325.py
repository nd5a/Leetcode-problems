# Container with Most Water

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # move the pointer of the smaller line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
