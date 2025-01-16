# Bitwise XOR of all Pairings

class Solution:
    def xorAllNums(self, nums1, nums2):
        def xor_array(arr):
            x = 0
            for a in arr:
                x ^= a
            return x
        
        ans = 0
        if len(nums2) % 2 == 1:
            ans ^= xor_array(nums1)
        if len(nums1) % 2 == 1:
            ans ^= xor_array(nums2)
        
        return ans