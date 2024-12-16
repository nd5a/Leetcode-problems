import heapq

class Solution:
    def getFinalState(self, nums, k, multiplier):
        N = len(nums)

        h = []
        for index, x in enumerate(nums):
            h.append([x, index])
        heapq.heapify(h)

        for _ in range(k):
            _, index = heapq.heappop(h)
            nums[index] *= multiplier
            heapq.heappush(h, [nums[index], index])
        
        return nums