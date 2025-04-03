# Maximum Value of an Ordered Triplet II

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
            max_num_i = prefix[j]
            max_num_k = suffix[j + 1]

            best = max(best, (max_num_i - nums[j]) * max_num_k)
        return best