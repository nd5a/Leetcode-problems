# Minimum Operations to Exceed Thresold Value II

import heapq

class Solution:
    def minOperations(self, nums, k):
        N = len(nums)

        heapq.heapify(nums)

        count = 0
        while len(nums) >= 2:
            if nums[0] >= k:
                return count
            count += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            heapq.heappush(nums, (x * 2 + y))
        
        if nums[0] >= k:
            return count
        return -1