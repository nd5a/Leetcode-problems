from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # Step 1: Precompute parity mismatches
        special_prefix = [0] * n
        for i in range(1, n):
            special_prefix[i] = special_prefix[i - 1] + (1 if nums[i] % 2 != nums[i - 1] % 2 else 0)

        # Step 2: Process each query efficiently
        results = []
        for l, r in queries:
            # If the subarray has only one element, it's always special
            if l == r:
                results.append(True)
            else:
                # Check parity mismatches in the range [l+1, r]
                if special_prefix[r] - special_prefix[l] == r - l:
                    results.append(True)
                else:
                    results.append(False)

        return results
