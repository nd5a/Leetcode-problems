# Count and Say

from itertools import groupby

class Solution:
    def countAndSay(self, n):
        current = "1"

        for _ in range(n -1):
            nxt = []
            for x, t in groupby(current):
                nxt.append(str(len(list(t))) + x)
            current = "".join(nxt)
        
        return current