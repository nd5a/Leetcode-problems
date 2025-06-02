# Candy

import collections
class Solution:
    def candy(self, ratings):
        N = len(ratings)

        indegree = [0] * N
        for i in range(N):
            for k in [i - 1, i + 1]:
                if 0 <= k < N and ratings[k]<ratings[i]:
                    indegree[i] += 1
        
        q = collections.deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        
        ans = [None] * N
        while len(q) > 0:
            current = q.popleft()

            candies = 1
            for k in [current - 1, current + 1]:
                if 0 <= k < N and ratings[k] < ratings[current]:
                    candies = max(candies, ans[k] + 1)
            ans[current] = candies

            for k in [current - 1, current + 1]:
                if 0 <= k < N and ratings[k] > ratings[current]:
                    indegree[k] -= 1
                    if indegree[k] == 0:
                        q.append(k)
        return sum(ans)