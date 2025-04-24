# Count Complete Subarrays in an array
class Solution:
    def countCompleteSubarrays(self, nums):
        N = len(nums)
        M = len(set(nums))
        count = 0

        for start in range(N):
            f= set()
            for end in range(start, N):
                f.add(nums[end])

                if len(f) == M:
                    count += 1
        return count