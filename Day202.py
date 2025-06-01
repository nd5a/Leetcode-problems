# Distribute Candies among Children II

class Solution:
    def distributeCandies(self, N, limit):
        if limit * 3 < N:
            return 0
        
        total = 0
        for i in range(min(N + 1, limit + 1)):
            candies_left = N -i

            if limit >= candies_left:
                total += candies_left + 1
            else:
                total += max(limit - (candies_left - limit) + 1, 0)
        return total