# Finding 3 - Digit Even Numbers

from collections import Counter
class Solution:
    def findNumbers(self, digits):
        result = set()
        count = Counter(digits)
        
        for i in range(100, 1000):
            if i % 2 == 0:
                c = Counter(map(int, str(i)))
                if all(count[d] >= c[d] for d in c):
                    result.add(i)
        return sorted(result)