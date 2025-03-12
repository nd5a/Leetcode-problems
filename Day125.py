# Number of Substrings Containing All three Characters

class Solution:
    def numberOfSubstrings(self, s):
        N = len(s)
        lasta = None
        lastb = None
        lastc = None

        total = 0
        for i in range(N):
            match s[i]:
                case 'a':
                    lasta =i
                case 'b':
                    lastb = i
                case 'c':
                    lastc = i
            
            if lasta is not None and lastb is not None and lastc is not None:
                total += min(lasta, lastb, lastc) + 1
        return total