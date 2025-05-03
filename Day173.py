# Minimum Domino Rotations for Equal Row

class Solution:
    def minDominoRotations(self, tops, bottoms):
        N = len(tops)
        INF = 10 ** 10

        best = INF
        for x in range(2):
            if x == 1:
                tops[0], bottoms[0] = bottoms[0], tops[0]
            
            count = x
            for i in range(N):
                if tops[0] == tops[i]:
                    continue
                if tops[0] == bottoms[i]:
                    count += 1
                    continue
                count = INF
            best = min(count, best)

            count = x
            for i in range(N):
                if bottoms[0] == bottoms[i]:
                    continue
                if bottoms[0] == tops[i]:
                    count += 1
                    continue
                count = INF
            best = min(count, best)

        if best >= INF:
            return -1
        return best