# Zero Array Transformation II

class Solution:
    def minZeroArray(self, nums, queries):
        N = len(nums)
        Q = len(queries)

        left = 0
        right = Q + 1

        def good(target):
            diff = [0] * (N +1)

            for l, r, v in queries[:target]:
                diff[l] += v
                diff[r + 1] -= v
            current = 0
            for i in range(N):
                current +=diff[i]

                if current < nums[i]:
                    return False
            return True
        while left < right:
            mid = (left + right) //2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        if left > Q:
            return -1
        return left