import heapq
class Solution:
    def pickGifts(self, gifts, k):
        h = []
        for g in gifts:
            h.append(-g)
        heapq.heapify(h)

        for _ in range(k):
            g = -heapq.heappop(h)
            heapq.heappush(h, -int(sqrt(g)))
        return -sum(h)