# Minimum Sum of Two Arrays After Replacing Zeros

class Solution:
    def minSum(self, nums1, nums2):
        asum, bsum, azero, bzero = sum(nums1), sum(nums2), 0, 0
        for i in nums1:
            if i == 0:
                azero += 1
        for i in nums2:
            if i == 0:
                bzero += 1
        
        if not azero:
            if asum < bsum + bzero: 
                return -1
        if not bzero:
            if bsum < asum + azero:
                return -1
        
        return max(asum + azero, bsum + bzero)