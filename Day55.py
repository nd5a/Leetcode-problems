# Maximum Score after Splitting a String

class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        n = len(s)

        # Iterate through all possible split points
        for i in range(1, n):  # Split at every position except the ends
            left = s[:i]
            right = s[i:]

            # Calculate the score
            left_zeros = left.count('0')
            right_ones = right.count('1')
            current_score = left_zeros + right_ones

            # Update the maximum score
            max_score = max(max_score, current_score)

        return max_score