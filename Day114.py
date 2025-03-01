# Apply Operations to Array

class Solution:
    def applyOperations(self, nums):
        N = len(nums)

        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i +1] = 0
        left = 0
        for right in range(N):
            while left < right and nums[left] != 0:
                left += 1
            
            if nums[right]  != 0:
                nums[left],nums[right] = nums[right], nums[left]
        return nums