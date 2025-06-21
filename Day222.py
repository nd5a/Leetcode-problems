# Minimum Deletion to Make String K-special

import collections
class Solution:
    def minimumDeletions(self, word, k):
        f = collections.Counter(word)

        v = list(sorted(f.values()))
        prefix = [0]
        for x in v:
            prefix.append(prefix[-1] + x)
        
        N = len(word)
        best = N

        smaller = 0
        right = 0
        for left in range(len(v)):
            if left - 1 >= 0:
                smaller += v[left - 1]
            right = max(right, left)

            while right < len(v) and v[right] - v[left] <= k:
                right += 1

            bigger = (prefix[len(v)] - prefix[right]) - ((v[left] + k) * (len(v) - (right))) 
            best = min(best, smaller + bigger)
        return best