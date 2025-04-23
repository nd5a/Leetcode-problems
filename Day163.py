# Count Largest Group

import collections
class Solution:
    def countLargestGroup(self, N):
        def get_sum(x):
            t = 0
            while x > 0:
                t += x % 10
                x //= 10
            return t
        
        f = collections.Counter()
        for i in range(1, N + 1):
            f[get_sum(i)] += 1
         
        m =max(f.values())
        count =0 

        for x in f.values():
            if x== m:
                count += 1
        return count