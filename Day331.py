# Taking Maximum Energy From the Mystic Dungeon

from typing import List

class Solution:
    def maximumEnergy(self, energy, k):
        n = len(energy)
        ans = float('-inf')
        
        # Start from last k indices and go backward
        for i in range(n - 1, n - k - 1, -1):
            total = 0
            j = i
            # Move backwards by step k
            while j >= 0:
                total += energy[j]
                ans = max(ans, total)
                j -= k
                
        return ans
