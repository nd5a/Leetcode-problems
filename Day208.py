# Lexicographical Minimum String After Removing Stars

import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        N = len(s)
        h = []
        removed = set()
        for i in range(N):
            if s[i] == "*":
                c, index = heapq.heappop(h)
                index = -index
                removed.add(index)
            else:
                heapq.heappush(h, (s[i], -i))
        
        ans = []
        for i in range(N):
            if s[i] != "*" and i not in removed:
                ans.append(s[i])
        return "".join(ans)