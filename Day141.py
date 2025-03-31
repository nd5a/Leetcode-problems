# Put Marbles in Bags

import heapq
from itertools import pairwise

class Solution:
    def putMarbles(self, weights, k):
        hsmall = []
        hlarge= []

        for x, y in pairwise(weights):
            v = x + y

            heapq.heappush(hsmall, -v)
            heapq.heappush(hlarge, v)

            while len(hsmall) > k - 1:
                heapq.heappop(hsmall)
            while len(hlarge) > k - 1:
                heapq.heappop(hlarge)
        return sum(hlarge) - -sum(hsmall)