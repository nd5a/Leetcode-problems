# Maximum Number of Tasks You Can Assign

from collections import deque
class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        def check(x):
            i = 0
            q = deque()
            p = pills
            for j in range(len(workers)- x, len(workers)):
                while i < x and tasks[i] <= workers[j] + strength:
                    q.append(tasks[i])
                    i += 1
                if not q:
                    return False
                if q[0] <= workers[j]:
                    q.popleft()
                elif p == 0:
                    return False
                else:
                    p -= 1
                    q.pop()
            return True
        
        tasks.sort()    
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left