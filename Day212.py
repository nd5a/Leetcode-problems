# Maximum Difference Between Even and Odd Frequency II

import collections
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        INF = 10 ** 10
        N = len(s)

        def calc(a,b):
            ca = 0
            cb = 0

            highest = -INF
            q = collections.deque()

            best =  [[INF] * 2 for _ in range(2)]
            q.append((0,0,0))
            prefix = 0
            for x in s:
                if x == a:
                    ca += 1
                    prefix += 1
                elif x == b:
                    cb += 1
                    prefix -= 1
                q.append((ca, cb,prefix))
                while len(q) > k:
                    if q[0][1] == cb:
                        break
                    qa, qb, p = q.popleft()
                    best[qa % 2][qb % 2] = min(best[qa % 2][qb % 2], p)
                
                highest = max(highest, prefix - best[(1 - ca) % 2][cb % 2])
            return highest
        best = -INF
        cs = set(s)

        for a in cs:
            for b in cs:
                if a != b:
                    best = max(best, calc(a,b))
        return best 