# Find the Number of Ways to Place People I

class Solution:
    def numberOfPairs(self, points):
        N = len(points)

        count = 0

        for i in range(N):
            ax, ay = points[i]
            for j in range(N):
                if i == j:
                    continue
                
                bx, by = points[j]

                if not (by >= ay and bx <= ax):
                    continue
                found = False

                for k in range(N):
                    if i == k or j == k:
                        continue
                    cx, cy = points[k]
                    if bx <= cx <= ax and by >= cy >= ay:
                        found = True
                if not found:
                    count += 1
        return count