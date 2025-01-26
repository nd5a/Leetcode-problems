# Maximum Employees to Be Invited to a Meeting

import collections

class Solution:
    def maximumInvitations(self, favorite):
        N = len(favorite)

        r = collections.defaultdict(set)
        for index, x in enumerate(favorite):
            r[x].add(index)
        
        done = [False] * N
        def go(x):
            done[x] = True
            mx = 0
            for v in r[x]:
                mx = max(mx, go(v) + 1)
            return mx
        
        res = 0
        for i in range(N):
            if i < favorite[i] and favorite[favorite[i]] == i:
                r[i].remove(favorite[i])
                r[favorite[i]].remove(i)
                
                max_left = go(i)
                max_right = go(favorite[i])

                res += 2 + max_left + max_right
        
        for i in range(N):
            if not done[i]:
                seen = {}

                step = 0
                current = i
                good = True
                while current not in seen:
                    if done[current]:
                        good = False
                        break
                    done[current] = True
                    seen[current] = step
                    step += 1
                    current = favorite[current]
                
                if good:
                    cycle = step - seen[current]
                    res = max(res, cycle)
        return res
        