# Count of Substrings Containing Every vowel and K Constants II

class Solution:
    def countOfSubstrings(self, word, k):
        N = len(word)
        vs = "aeiou"

        total = 0

        v=[0] * 5
        vcount =0
        kcount= 0
        degree = 0

        left = 0
        for right in range(N):
            if word[right] in vs:
                if v[vs.index(word[right])] == 0:
                    vcount += 1
                    if vcount == 5 and kcount== k:
                        degree = 1
                
                v[vs.index(word[right])] += 1
                if kcount == k:
                    while vcount == 5:
                        if word[left] not in vs:
                            break
                        if v[vs.index(word[left])] == 1:
                            break
                        v[vs.index(word[left])] -= 1
                        degree += 1
                        if v[vs.index(word[left])] == 0:
                            vcount -= 1
                        left += 1
                    
                    total += degree
            else:
                kcount += 1

                while kcount > k:
                    if word[left] in vs:
                        v[vs.index(word[left])] -= 1
                        if v[vs.index(word[left])] == 0:
                            vcount -= 1
                    else:
                        kcount -= 1
                    left += 1
                if kcount == k:
                    degree = 0
                    while vcount == 5:
                        degree += 1
                        if word[left] not in vs:
                            break
                        if v[vs.index(word[left])] == 1:
                            break
                        
                        v[vs.index(word[left])] -= 1
                        if v[vs.index(word[left])] == 0:
                            vcount -= 1
                        left += 1
                    total += degree
        return total