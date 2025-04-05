# Sum of All Subset XOR Totals

class Solution:
    def subsetXORSum(self, nums):
        N = len(nums)
        total = 0

        def suffixXor(index, current):
            if index == N:
                nonlocal total
                total += current
                return
            
            suffixXor(index + 1, current ^ nums[index])

            suffixXor(index + 1, current)
        suffixXor(0, 0)
        return total