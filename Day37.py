# hello 37
from collections import deque
class Solution:
    def continuousSubarrays(self, nums) -> int:

        n = len(nums)
        count = 0

        left = 0
        max_deque = deque()  # To track the maximum value in the window
        min_deque = deque()  # To track the minimum value in the window

        for right in range(n):
            # Update max_deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Update min_deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Shrink the window if the condition is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Add the number of subarrays ending at 'right'
            count += (right - left + 1)

        return count