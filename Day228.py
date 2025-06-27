# Longest Subsequence Repeated k Times

import collections
class Solution:
    def longestSubsequenceRepeatedK(self, s, k):
        N = len(s)
        cs = list(sorted(set(s)))

        def calculate(current):
            index = 0
            count = 0
            for i in range(N):
                if s[i] == current[index]:
                    index += 1
                
                if index >= len(current):
                    count += 1
                    index = 0
            return count
        
        best = ""

        q = collections.deque()
        q.append("")

        while len(q) > 0:
            current = q.popleft()

            for x in cs:
                w = current + x
                if calculate(w) >= k:
                    q.append(w)
            best = current
        
        return best