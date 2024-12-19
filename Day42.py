# Max Chunks to make Sorted

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = 0
        chunks = 0

        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])
            # If the maximum value so far matches the current index,
            # we can split here as all elements are in place.
            if max_so_far == i:
                chunks += 1

        return chunks
