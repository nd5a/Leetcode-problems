# Longest Nice Subarray

class Solution:
    def longestNiceSubarray(self, nums):
        left = 0  
        bitwise_or = 0  
        max_length = 0  
        
        for right in range(len(nums)):
            while (bitwise_or & nums[right]) != 0:
                bitwise_or ^= nums[left]  
                left += 1 
            
            bitwise_or |= nums[right]
            
            max_length = max(max_length, right - left + 1)
        
        return max_length