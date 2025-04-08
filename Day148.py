# Minimum Number of Operations to Make Elements in Array Distinct

class Solution:
    def minimumOperations(self, nums):
        N = len(nums)

        max_ops = ((N + 2) // 3)

        seen = set()
        for i in range(max_ops):
            offset = (max_ops - i- 1) * 3
            good = True

            for j in range(3):
                if offset + j < N:
                    if nums[offset + j] in seen:
                        good = False
                    seen.add(nums[offset + j])
            if not good:
                return max_ops - i
        return 0