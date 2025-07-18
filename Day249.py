# Minimum Difference in Sums after Removal of Elements

from sortedcontainers import SortedList

class Solution:
    def minimumDifference(self, nums):
        N = len(nums)
        N3 = N // 3

        sum_left = sum_right = 0
        left = SortedList()
        right = SortedList()

        # First N elements on the left side
        for i in range(N3):
            sum_left += nums[i]
            left.add(nums[i])

        # First N elements on the right side
        for i in range(N3, N):
            sum_right += nums[i]
            right.add(nums[i])
        
        # these are the numbers that didn't make the list, but still the right side
        floating = SortedList()
        
        # keep N eleements on the left, and right.
        for _ in range(N3):
            x = right[0]
            right.remove(x)
            sum_right -= x

            floating.add(x)
        
        # now begin the sliding window
        best = sum_left - sum_right

        #print left, floating, right
        for i in range(N3, 2 * N3):
            if nums[i] in right:
                right.remove(nums[i])
                sum_right -= nums[i]

                # add one from the floating to maintain there are N elements
                f = floating[-1]
                floating.remove(f)

                right.add(f)
                sum_right += f
            else:
                floating.remove(nums[i])
            
            left.add(nums[i])
            sum_left += nums[i]
            
            # now left has N + 1 elements, so remove the biggest
            b = left[-1]
            left.remove(b)
            sum_left -= b

            best = min(best, sum_left - sum_right)
        return best