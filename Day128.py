# House Robber IV

class Solution:
    def minCapability(self, nums, k):
        left = 1
        right = max(nums)

        def good(target):
            count = 0
            skip= False
            for x in nums:
                if skip:
                    skip = False
                    continue
                
                if x <= target:
                    skip = True
                    count += 1
            return count >= k
        
        while left<right:
            mid = (left + right) //2

            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left