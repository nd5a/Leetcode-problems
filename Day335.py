# Adjacent Increasing Subarrays Detection I

class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        streaks = []
        count = 0
        last = -10000
        N = len(nums)

        for x in nums:
            if x > last:
                count += 1
            else:
                count = 1
            
            last= x
            streaks.append(count)
        
        for i in range(k, N):
            if streaks[i] == k and streaks[ i - k] >= k:
                return True
            if streaks[i] >= k * 2:
                return True
        return False