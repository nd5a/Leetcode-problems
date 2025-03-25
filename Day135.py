# Check if Grid can be Cut into Sections

import collections

class Solution:
    def checkValidCuts(self, n, rectangles):
        def can_cut(segments):
            events = collections.Counter()

            for start, end in segments:
                events[2 * start] += 1
                events[2 * end - 1] -=1
        
            cuts = 0
            current = 0
            for t in sorted(events.keys()):
                if current > 0 and current + events[t] == 0:
                    cuts += 1
                current += events[t]
            return cuts >= 3
        xs = [] 
        ys = []
        for sx, sy, ex, ey in rectangles:
            xs.append((sx, ex))
            ys.append((sy, ey))
        return can_cut(xs) or can_cut(ys)