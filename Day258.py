# Count Hills and Valleys in Array

class Solution:
    def countHillValley(self, nums):
        arr = []
        for x in nums:
            if len(arr) == 0 or arr[-1] != x:
                arr.append(x)
        nums = arr
        
        N = len(nums)

        count = 0
        for i in range(1, N - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                count += 1
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                count += 1
        return count