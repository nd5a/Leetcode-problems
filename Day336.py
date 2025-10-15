# Adjacent Increasing Subarrays Detection II

class Solution:
    def maxIncreasingSubarrays(self, nums):
        INF = 10 ** 20

        best = 0
        streaks = []
        count = 0
        last = -INF

        for x in nums:
            if x > last:
                count += 1
            else:
                count = 1
            
            last = x
            streaks.append(count)
        
        best = max(streaks) // 2

        for i in range(len(streaks)):
            if streaks[i] <= best:
                continue
            if i - streaks[i] < 0:
                continue
            
            if streaks[i - streaks[i]] >= streaks[i]:
                best = max(best, streaks[i])
        return best