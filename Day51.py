class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        N = len(nums)
        # Step 1: Compute the sums of all subarrays of size k
        subarray_sums = [0] * (N - k + 1)
        current_sum = sum(nums[:k])
        subarray_sums[0] = current_sum
        for i in range(1, N - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            subarray_sums[i] = current_sum

        # Step 2: Find the maximum sum of subarrays for the left, middle, and right
        left_max = [0] * (N - k + 1)
        right_max = [0] * (N - k + 1)

        # Fill left_max array
        max_index = 0
        for i in range(N - k + 1):
            if subarray_sums[i] > subarray_sums[max_index]:
                max_index = i
            left_max[i] = max_index

        # Fill right_max array (backward traversal)
        max_index = N - k
        for i in range(N - k, -1, -1):
            if subarray_sums[i] >= subarray_sums[max_index]:
                max_index = i
            right_max[i] = max_index

        # Step 3: Find the best middle subarray and compute the result
        max_total = 0
        result = []
        for middle in range(k, N - 2 * k + 1):
            left = left_max[middle - k]
            right = right_max[middle + k]
            total = subarray_sums[left] + subarray_sums[middle] + subarray_sums[right]
            if total > max_total:
                max_total = total
                result = [left, middle, right]
            elif total == max_total:
                # If there is a tie, pick the lexicographically smaller one
                result = min(result, [left, middle, right])

        return result