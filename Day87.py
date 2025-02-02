# Check if Array is Sorted and rotated

class Solution:
    def check(self, nums):
        N = len(nums)

        first = None
        for i in range(N):
            if nums[(i - 1) % N] > nums[i]:
                first = i
                break

        if first is None:
            first = 0
        
        for offset in range(N - 1):
            if nums[(i + offset) % N] > nums[(i + offset + 1) % N]:
                return False
        return True