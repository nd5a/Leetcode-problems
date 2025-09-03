# Find the Number to ways to place People I

import collections
class Solution:
    def numberOfPairs(self, points):
        N = len(points)
        INF = 10 ** 20

        points.sort()
        
        p = collections.defaultdict(list)
        sweep = collections.defaultdict(int)

        count = 0
        prevx = -INF
        
        for i, (x, y) in enumerate(points):
            if x != prevx:
                prevx = x
                sweep = collections.defaultdict(int)
            else:
                count += 1
            stack = []

            for px in p.keys():
                while sweep[px] < len(p[px]) and p[px][sweep[px]] < y:
                    sweep[px] += 1
                
                if sweep[px] < len(p[px]):
                    while len(stack) > 0 and stack[-1] >= p[px][sweep[px]]:
                        stack.pop()
                    stack.append(p[px][sweep[px]])


            if i + 1 < len(points) and points[i + 1][0] == x:
                ny = points[i + 1][1]
            
                while len(stack) > 0 and stack[-1] >= ny:
                    stack.pop()
            
            count += len(stack)
            p[x].append(y)
        return count

