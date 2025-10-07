# Avoid Flood in The City
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains):
        N = len(rains)

        ans = [-1] * N
        full = {}

        dry_indices = SortedList()

        for index, lake in enumerate(rains):
            if lake == 0:
                dry_indices.add(index)
                continue
            
            if lake not in full:
                full[lake] = index
                continue
            
            sindex = dry_indices.bisect_left(full[lake])

            if sindex >= len(dry_indices):
                return []
            
            dry_day = dry_indices[sindex]
            ans[dry_day] = lake
            dry_indices.remove(dry_day)
            full[lake] = index

        for x in dry_indices:
            ans[x] = 100
        return ans