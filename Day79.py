# Make Lexicographically Smallest Array by Swapping Elements

class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        INF = 10 ** 20
        N = len(nums)

        pairs = []
        for index, x in enumerate(nums):
            pairs.append((x, index))
        pairs.sort()

        ans = [None] * N
    
        def process(xs, indices):
            indices.sort()
            for i, x in enumerate(xs):
                ans[indices[i]] = x

        prev = -INF
        xs = []
        indices = []
        for x, index in pairs:
            if x - prev > limit:
                process(xs, indices)
                xs = []
                indices =[]
            xs.append(x)
            indices.append(index)
            prev = x
        else:
            process(xs, indices)
        
        return ans