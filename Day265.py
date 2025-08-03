# Maximum Fruits Harvested After at Most K steps

import bisect
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        if n == 0:
            return 0
        
        positions = [f[0] for f in fruits]
        amounts = [f[1] for f in fruits]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + amounts[i]
        
        max_fruits = 0
        
        low1 = max(0, startPos - k)
        high1 = startPos
        i1 = bisect.bisect_left(positions, low1)
        j1 = bisect.bisect_right(positions, high1) - 1
        if i1 <= j1:
            total1 = prefix[j1 + 1] - prefix[i1]
            if total1 > max_fruits:
                max_fruits = total1
        
        low2 = startPos
        high2 = startPos + k
        i2 = bisect.bisect_left(positions, low2)
        j2 = bisect.bisect_right(positions, high2) - 1
        if i2 <= j2:
            total2 = prefix[j2 + 1] - prefix[i2]
            if total2 > max_fruits:
                max_fruits = total2
        
        for i in range(n):
            if fruits[i][0] > startPos:
                break
            left_pos = fruits[i][0]
            steps_used = startPos - left_pos
            if steps_used > k:
                continue
            max_right = k - startPos + 2 * left_pos
            j = bisect.bisect_right(positions, max_right) - 1
            if j < i:
                continue
            total = prefix[j + 1] - prefix[i]
            if total > max_fruits:
                max_fruits = total
        
        for i in range(n - 1, -1, -1):
            if fruits[i][0] < startPos:
                break
            right_pos = fruits[i][0]
            steps_used = right_pos - startPos
            if steps_used > k:
                continue
            min_left = 2 * right_pos - startPos - k
            j = bisect.bisect_left(positions, min_left)
            if j > i:
                continue
            total = prefix[i + 1] - prefix[j]
            if total > max_fruits:
                max_fruits = total
        
        return max_fruits