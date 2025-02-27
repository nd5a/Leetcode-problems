# Length of longest Fibonacci Subsequence

class Solution:
    def lenLongestFibSubseq(self, arr):
        N = len(arr)
        s = set(arr)
        seen = set()

        best = 0
        for i1 in range(N):
            for i2 in range(i1 + 1, N):
                x1 = arr[i1]
                x2 = arr[i2]
                current = 2

                x3 = x1 + x2
                while x3 in s:
                    x1, x2= x2, x3
                    if (x1, x2) in seen:
                        break
                    seen.add((x1, x2))
                    x3 = x1 + x2
                    current += 1
                
                if current >= 3:
                    best = max(best, current)
        return best