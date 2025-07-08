# Maximum Number of Events That Can Be Attended II

import heapq
import collections
class Solution:
    def maxValue(self, e, k):
        INF = 10 ** 20
        events = collections.defaultdict(list)

        for st, ed, v in e:
            events[st].append((ed,v))
        
        best = [0] * (k + 1)

        events[INF]
        h = []
        for t in sorted(events.keys()):
            while len(h) > 0 and h[0][0] <= t:
                _, cbest = heapq.heappop(h)
                for ck in range(1, k + 1):
                    best[ck] = max(best[ck], cbest[ck])
            
            for ed, v in events[t]:
                cbest = [0] * (k + 1)
                for ck in range(k):
                    cbest[ck + 1] = best[ck] + v
                heapq.heappush(h, (ed + 1, cbest))
        return max(best)