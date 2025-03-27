# Minimum Index of a Valid Split

class Solution:
    def minimumIndex(self, nums):
        N = len(nums)

        most_common = None
        count = 0
        for x in nums:
            if most_common == x:
                count += 1
            else:
                count -=1
                if count < 0:
                    count = 1
                    most_common = x
        count = 0
        for x in nums:
            if x == most_common:
                count += 1
            
        if count * 2 <= N:
            return -1
        
        left = 0
        right = count

        for index, x in enumerate(nums[:-1]):
            if x == most_common:
                left += 1
                right -= 1

            if left * 2 > (index + 1) and right * 2> (N - index - 1):
                return index
        else:
            return -1