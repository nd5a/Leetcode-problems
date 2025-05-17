# Sort Colors

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        zero_pointer = 0
        two_pointer = N - 1

        current_pointer = 0
        while current_pointer <= two_pointer:
            if nums[current_pointer] == 0:
                nums[zero_pointer], nums[current_pointer] = nums[current_pointer], nums[zero_pointer]
                zero_pointer += 1
                current_pointer += 1
            elif nums[current_pointer] == 2:
                nums[two_pointer], nums[current_pointer] = nums[current_pointer], nums[two_pointer]
                two_pointer -= 1
            else:
                current_pointer += 1