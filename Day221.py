# Maximum Manhattan Distance After K Changes

class Solution:
    def maxDistance(self, s, k):
        n = len(s)
        base_E = base_N = base_S = base_W = 0
        ans = 0
        for i in range(n):
            if s[i] == 'E':
                base_E += 1
            elif s[i] == 'N':
                base_N += 1
            elif s[i] == 'S':
                base_S += 1
            elif s[i] == 'W':
                base_W += 1
            
            c_prime = min(k, i + 1)
            base_AB = base_E + base_N
            base_CD = base_S + base_W
            base_AC = base_E + base_S
            base_BD = base_N + base_W
            
            t_val = i + 1
            
            X_min = base_AB - min(base_AB, c_prime)
            X_max = base_AB + min(base_CD, c_prime)
            Y_min = base_AC - min(base_AC, c_prime)
            Y_max = base_AC + min(base_BD, c_prime)
            
            cand1 = max(abs(2 * X_min - t_val), abs(2 * X_max - t_val))
            cand2 = max(abs(2 * Y_min - t_val), abs(2 * Y_max - t_val))
            candidate = max(cand1, cand2)
            
            if candidate > ans:
                ans = candidate
        
        return ans