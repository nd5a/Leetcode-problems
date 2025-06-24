# Find All K - Distinct indices in an array

import collections
class Solution:
    def findKDistantIndices(self, nums, key, k):
        # l = len(nums)
        # l1 = []
        # for i in range(l):
        #     if nums[i] == key and len(set(nums)) == 1 and nums[i] == key and nums[i] == k:
        #         l1.append(i)
        #     else:
        #         if nums[i] == key:
        #             for j in range(l):
        #                 if abs(j - i) <= k:
        #                     l1.append(j)
        # return list(set(l1))
        
        N = len(nums)
        indices = collections.deque()
        for i in range(N):
            if nums[i] == key:
                indices.append(i - k)
        
        rightmost = -1
        ans = []

        for i in range(N):
            while len(indices) > 0 and indices[0] <=i:
                rightmost = max(rightmost, indices[0] + k + k)
                indices.popleft()
            
            if i <= rightmost:
                ans.append(i)
        return ans