# Alternating Groups II

class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        N = len(colors)
        colors = colors +colors
        
        for i in range(N * 2):
            if i % 2==1:
                colors[i]= 1-colors[i]
        
        count = 0
        zero_inside=0
        for right in range(N +k -1):
            if colors[right] == 0:
                zero_inside +=1
            left = right - k + 1
            if left -1>=0 and colors[left-1] == 0:
                zero_inside -=1
            if left >= 0:
                if zero_inside == 0 or zero_inside == k:
                    count += 1
        return count