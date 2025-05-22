# Zero Transformations III

import collections
import heapq

class Solution:
    def maxRemoval(self, nums, queries):
        q = collections.deque(sorted(queries))

        good_to_use = []
        currently_using =[]

        count= 0
        for index, x in enumerate(nums):
            while len(q) > 0 and q[0][0] <= index:
                heapq.heappush(good_to_use, -q[0][1])
                q.popleft()
            
            while len(currently_using) > 0:
                if currently_using[0] < index:
                    heapq.heappop(currently_using)
                else:
                    break
            
            while len(currently_using)< x:
                if len(good_to_use) == 0:
                    return -1
                
                r = -heapq.heappop(good_to_use)
                if r < index:
                    continue
                
                heapq.heappush(currently_using, r)
                count += 1

        return len(queries) - count