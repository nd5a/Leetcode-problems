# Total Characters in string After Transformations II

identify = [[0] * 26 for _ in range(26)]
for i in range(26):
    identify[i][i] = 1

class Solution:
    def lengthAfterTransformations(self, s, t, nums):
        MOD = 10 ** 9 + 7
        def mat_power(matrix, power):
            if power == 0:
                return identify
            if power == 1:
                return matrix
            
            m = mat_power(matrix, power // 2)
            if power % 2 == 0:
                return mat_mult(m,m)
            else:
                return mat_mult(mat_mult(m,m), matrix)
        
        def mat_mult(a,b):
            aR = len(a)
            aC = len(a[0])
            bR = len(b)
            bC = len(b[0])

            assert(aC == bR)
            res = [[0] * bC for _ in range(aR)]

            for i in range(aR):
                for j in range(aC):
                    for k in range(bC):
                        res[i][k] += a[i][j] * b[j][k]
            for i in range(aR):
                for j in range(bC):
                    res[i][j] %= MOD
            return res
        
        f = [[0] * 26]
        for c in s:
            f[0][ord(c) - ord('a')] += 1
        
        trans = [[0] * 26 for _ in range(26)]
        for index, x in enumerate(nums):
            for i in range(x):
                trans[index][(index + i + 1) % 26] += 1
        r = mat_mult(f, mat_power(trans, t))
    
        return sum(r[0]) % MOD