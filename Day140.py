# Partitioon Labels

class Solution:
    def partitionLabels(self, s):
        first = {}
        last = {}
        for index, c in enumerate(s):
            if c not in first:
                first[c] = index
            last[c] = index
        
        arr = []
        for c in first.keys():
            arr.append((first[c], last[c]))
        arr.sort()
        
        right_most = -1
        needed = []
        current_left = -1

        for f, l in arr:
            if right_most > f:
                right_most = max(right_most, l)
            else:
                needed.append(right_most - current_left + 1)
                current_left = f
                right_most = l
        
        needed.append(right_most - current_left + 1)
        return needed[1:]