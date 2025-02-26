# Maximum Absolute Sum of Any Subarray

class Solution:
    def maxAbsoluteSum(self, nums):
        # kadane's algorithm

        def kadane(arr, m = 1):
            best =0
            current = 0
            for x in arr:
                x *= m
                if current < 0:
                    current = 0
                current += x
                best = max(best, current)
            return best
        return max(kadane(nums), kadane(nums, -1))