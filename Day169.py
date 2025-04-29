# Count Subarrays where the maximum element is less than k times

class Solution:
    def countSubarrays(self, nums, k):
        N = len(nums)

        mx = max(nums)
        count = 0
        left = 0
        total = 0
        for right in range(N):
            if nums[right] == mx:
                count += 1
            
            while count >= k:
                if nums[left] == mx:
                    count -= 1
                left += 1
            total += left
        return total