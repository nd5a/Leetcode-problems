# Longest Strictly Increasing or Strictly Decreasing Subarray

class Solution:
    def longestMonotonicSubarray(self, nums):
        max_length = 1
        inc = 1
        dec = 1

        # Iterate through the array
        for i in range(1, len(nums)):
            # If the current element is greater than the previous, increment the increasing count
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1  # Reset the decreasing count
            # If the current element is smaller than the previous, increment the decreasing count
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1  # Reset the increasing count
            else:
                # Reset both counts when the current element is equal to the previous
                inc = 1
                dec = 1

            # Update the maximum length
            max_length = max(max_length, inc, dec)

        return max_length