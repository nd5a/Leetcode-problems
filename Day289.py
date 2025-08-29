# Alice and Bob playing Flower Game

class Solution:
    def flowerGame(self, N, M):
        
        evens_odds = ((N + 1) // 2) * (M // 2)
        odds_evens = (N // 2) * ((M + 1) // 2)

        return evens_odds + odds_evens