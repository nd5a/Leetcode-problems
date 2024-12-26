# Target Sum

class Solution:
    def findTargetSumWays(self, nums, target):
        N = len(nums)
        # @cache
        def evaluate(index, current):
            if index == N:
                if current == target:
                    return 1
                return 0
            
            total = 0
            total += evaluate(index + 1, current + nums[index])
            total += evaluate(index + 1, current - nums[index])
            return total
        return evaluate(0, 0)