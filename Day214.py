# Minimizes the Maximum Difference of Pairs

class Solution:
    def minimizeMax(self, nums, p):
        if p == 0:
            return 0
        
        nums.sort()
        n = len(nums)
        
        def can_form_pairs(max_diff):
            count = 0 
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  
                else:
                    i += 1 
            return count >= p
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                right = mid 
            else:
                left = mid + 1
        
        return left