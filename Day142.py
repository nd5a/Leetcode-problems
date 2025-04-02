# Maximum Value of an Ordered Triplet I

class Solution:
    def maximumTripletValue(self, nums):
        N = len(nums)

        prefix = [0]
        for x in nums:
            prefix.append(max(prefix[-1], x))
        
        suffix = [0]
        for x in nums[::-1]:
            suffix.append(max(suffix[-1], x))
        suffix.reverse()

        best = 0
        for j in range(N):
            max_nums_i = prefix[j]
            max_nums_k = suffix[j + 1]

            best = max(best, (max_nums_i - nums[j]) * max_nums_k)
        return best