class Solution:
    def findScore(self, nums):
        N = len(nums)
        rank = [i for i in range(N)]
        rank.sort(key = lambda i: (nums[i],i))

        marked = [False] * N

        score = 0
        for r in rank:
            if not marked[r]:
                score += nums[r]
                marked[r] = True
                if r - 1 >= 0:
                    marked[r - 1] =True
                if r + 1 < N:
                    marked[r + 1] = True
        return score