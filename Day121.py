# Minimum Recolors to Get K Consecutive Black Blocks

class Solution:
    def minimumRecolors(self, blocks, k):
        N = len(blocks)

        best = N
        white_in_window = 0

        for i in range(N):
            if blocks[i] == "W":
                white_in_window += 1
            if i - k>=0 and blocks[i - k] == "W":
                white_in_window -= 1
            if i >= k -1:
                best = min(best, white_in_window)
        return best