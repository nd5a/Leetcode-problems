# Lexicographically Smallest Equivalent String

import collections
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj_list = collections.defaultdict(list)

        best = {}
        for x, y in zip(s1, s2):
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        earliest = {}
        for c in string.ascii_lowercase:
            if c not in earliest:
                q = collections.deque()
                earliest[c] = c
                q.append(c)

                while len(q) > 0:
                    current = q.popleft()

                    for v in adj_list[current]:
                        if v not in earliest:
                            earliest[v] = c
                            q.append(v)
        ans = []
        for c in baseStr:
            ans.append(earliest[c])
        return "".join(ans)