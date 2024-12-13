# Finding Champ II

class Solution:
    def findChampion(self, n, edges):
        lose = [False] * n
        for u, v in edges:
            lose[v] = True
        
        count = 0
        champ = None
        for i in range(n):
            if not lose[i]:
                count+=1
                champ = i
        
        if count != 1:
            return -1
        return champ