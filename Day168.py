# Count Subarrays with score less than k

class Solution:
    def countSubarrays(self, nums, k):
        N = len(nums)
        prefix = [0]

        for x in nums:
            prefix.append(x + prefix[-1])
        
        def good(left, right):
            return ((prefix[right + 1]- prefix[left]) * (right - left + 1))<k
    
        total = 0
        for i in range(N):
            if nums[i] >= k:
                continue
            
            left = i
            right = N - 1

            while left < right:
                mid = (left + right + 1)// 2

                if good(i, mid):
                    left = mid
                else:
                    right = mid - 1
            total += (right - i +1)
        return total