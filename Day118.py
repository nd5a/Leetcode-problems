# Count Total Number of Colored Cells
class Solution:
    def coloredCells(self, N):
        return 1 + 4*(N-1) + 2 * (N-2) * (N-1)