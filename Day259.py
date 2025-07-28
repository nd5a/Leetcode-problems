# Count Number of Maximum Bitwise-OR Subsets

class Solution:
    def countMaxOrSubsets(self, nums):
        N = len(nums)
        or_sum = 0
        for x in nums:
            or_sum |= x

        count = 0 

        def calc(index, current):
            if index == N:
                if current == or_sum:
                    nonlocal count
                    count += 1
                return
            
            calc(index + 1, current)
            calc(index + 1, current | nums[index])
        calc(0, 0)
        return count