# Maximum Candies you can Get from boxes

import collections

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        N = len(status)

        owned = [False] * N
        opened = [False] * N
        added = [False] * N

        for i in range(N):
            opened[i] = (status[i] == 1)
        for b in initialBoxes:
            owned[b] = True
        
        q = collections.deque()
        for i in range(N):
            if owned[i] and opened[i]:
                q.append(i)
                added[i] = True
        
        total = 0
        while len(q) > 0:
            b = q.popleft()

            total += candies[b]
            for k in keys[b]:
                opened[k] = True
                if owned[k] and opened[k] and not added[k]:
                    q.append(k)
                    added[k] = True

            for k in containedBoxes[b]:
                owned[k] = True
                if owned[k] and opened[k] and not added[k]:
                    q.append(k)
                    added[k] = True
        return total