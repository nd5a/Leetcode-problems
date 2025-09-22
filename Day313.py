# Count Elements With Maximum Frequency

from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(v for v in freq.values() if v == max_freq)