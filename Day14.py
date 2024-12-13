class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n < k:
            return 0  # If the array length is less than k, no valid subarray can exist

        max_sum = 0
        current_sum = 0
        window = set()
        left = 0

        for right in range(n):
            # Remove duplicates if the current element already exists in the window
            while nums[right] in window:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Add the current element
            window.add(nums[right])
            current_sum += nums[right]

            # If the window size exceeds `k`, shrink it
            if right - left + 1 > k:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # If the window size is exactly `k`, update the maxDay15.py_sum
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
