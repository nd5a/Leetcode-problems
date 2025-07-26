# Maximize Subarrays After Removing One Conflicting Pair

import collections
class Solution:
    def maxSubarrays(self, N, conflictingPairs):
        barriers = collections.defaultdict(list)

        for index, (a, b) in enumerate(conflictingPairs):
            if a > b:
                a, b = b, a
            
            barriers[b].append((a, index))
        
        contributions = [0] * N

        last_barrier = (0, -1)
        second_barrier = (0, -1)

        gains = collections.Counter()

        for i in range(1, N + 1):
            for a, index in barriers[i]:
                if a > last_barrier[0]:
                    second_barrier = last_barrier
                    last_barrier = (a, index)
                elif a > second_barrier[0]:
                    second_barrier = (a, index)
                
            contributions[i - 1] = i- last_barrier[0]

            # if we remove last_barrier, we get second_barrier
            gains[last_barrier[1]] += last_barrier[0] - second_barrier[0]
        
        total = sum(contributions)
        return total + max(gains.values())
        