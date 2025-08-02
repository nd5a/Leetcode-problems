# Rearranging Fruits

import collections
class Solution:
    def minCost(self, basket1, basket2):
        # Step 1: Sort both baskets to prepare for comparison
        basket1.sort()
        basket2.sort()

        # Step 2: Get the smallest fruit cost from both baskets
        mn = min(min(basket1), min(basket2))

        # Step 3: Count all fruit occurrences from both baskets
        f = collections.Counter(basket1 + basket2)
        for k, v in f.items():
            if v % 2 == 1:
                return -1  # Odd count means it’s impossible to make them equal

        # Step 4: Get the excess fruits from both baskets
        f1 = collections.Counter(basket1) - collections.Counter(basket2)
        f2 = collections.Counter(basket2) - collections.Counter(basket1)

        # Step 5: Build the list of excess elements to be swapped
        considers = []
        for k, v in list(f1.items()) + list(f2.items()):
            considers += [k] * (v // 2)
        considers.sort()

        # Step 6: Calculate minimum cost using greedy strategy
        score = 0
        for i in range(len(considers) // 2):
            score += min(considers[i], mn * 2)
        return score
