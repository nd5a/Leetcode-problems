# Compare version Numbers

class Solution:
    def compareVersion(self, version1, version2):
        def conv(s):
            return [int(x) for x in s.split(".")]
        
        def p(v, m):
            while len(v) < m:
                v.append(0)
            return v

        v1, v2 = conv(version1), conv(version2)
        m = max(len(v1), len(v2))
        v1, v2 = p(v1, m), p(v2, m)
        
        if v1 == v2:
            return 0
        elif v1 > v2:
            return 1
        return -1