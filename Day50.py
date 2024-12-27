class Solution:
    def maxScoreSightseeingPair(self, values):
        N = len(values) 
        INF = 10 ** 20
        best_score = 0  
        best_iscore = -INF
        for index in range(N):
            j = index
            jscore = values[j] - j

            best_score = max(best_score, best_iscore + jscore)

            i = index
            best_iscore = max(best_iscore, values[i] + i)
        return best_score