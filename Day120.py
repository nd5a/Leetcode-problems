# Closest Prime Numbers in Range

from typing import List
import bisect

M = 10**6  # Set M to 10^6 as per the problem constraints

# Precompute prime numbers using the Sieve of Eratosthenes
prime = [True] * (M + 1)
prime[0] = prime[1] = False
p = []

for i in range(2, M + 1):
    if prime[i]:
        p.append(i)
        for j in range(i * 2, M + 1, i):
            prime[j] = False

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        INF = float('inf')

        best = INF
        besti = None
        past = -INF

        # Find the index of the first prime >= left
        index = bisect.bisect_left(p, left)

        # If index is out of bounds or the first prime is greater than right, return [-1, -1]
        if index >= len(p) or p[index] > right:
            return [-1, -1]

        # Iterate through prime numbers in the range
        while index < len(p) and p[index] <= right:
            if past != -INF and (p[index] - past) < best:
                best = p[index] - past
                besti = past
            past = p[index]
            index += 1

        if besti is None:
            return [-1, -1]

        return [besti, besti + best]
