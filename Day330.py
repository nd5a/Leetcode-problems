# Find the maximum Amount of Time to Brew Points

fmax = lambda x, y: x if x > y else y

class Solution:
    def minTime(self, skill, mana):
        S = len(skill)
        M = len(mana)

        t = [0] * (S + 1)
        for m in mana:
            current = 0
            delta = 0
            for i, s in enumerate(skill):
                delta = fmax(delta, t[i + 1] - current)
                current += s * m
            
            current = delta
            for i, s in enumerate(skill):
                current += s* m
                t[i + 1] = current
        
        return t[-1]    