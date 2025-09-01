# Maximum Average pass Ration
import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        N = len(classes)
        h = []
        for p, t in classes:
            heapq.heappush(h, (-(((p + 1)/ (t + 1)) - (p / t)), p, t))
        
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(h)
            p += 1
            t += 1
            heapq.heappush(h, (-(((p + 1)/ (t + 1)) - (p / t)), p, t))

        total_ratio = 0.0
        for _, p, t in h:
            total_ratio += (p / t)

        return total_ratio / N