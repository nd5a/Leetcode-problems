# Shortest Common Supersequence

class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        N1 = len(str1)
        N2 = len(str2)

        SAME = 0
        ADD_S1 = 1
        ADD_S2 = 2

        # Cache for memoization
        has_cache = [[False] * (N2 + 1) for _ in range(N1 + 1)]
        cache = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        nxt = [[0] * (N2 + 1) for _ in range(N1 + 1)]

        def longest_common_subsequence(index1, index2):
            if index1 == N1 or index2 == N2:
                return 0
            
            if has_cache[index1][index2]:
                return cache[index1][index2]
            
            best = 0
            if str1[index1] == str2[index2]:
                v = longest_common_subsequence(index1 + 1, index2 + 1) + 1
                if best < v:
                    best = v
                    nxt[index1][index2] = SAME
            else:
                v1 = longest_common_subsequence(index1 + 1, index2)
                v2 = longest_common_subsequence(index1, index2 + 1)
                if v1 > v2:
                    best = v1
                    nxt[index1][index2] = ADD_S1
                else:
                    best = v2
                    nxt[index1][index2] = ADD_S2
            
            has_cache[index1][index2] = True
            cache[index1][index2] = best
            return best

        # Compute the LCS length
        C = longest_common_subsequence(0, 0)

        # Build the shortest common supersequence
        ans = []
        i1, i2 = 0, 0
        while i1 < N1 and i2 < N2:
            if nxt[i1][i2] == SAME:
                ans.append(str1[i1])
                i1 += 1
                i2 += 1
            elif nxt[i1][i2] == ADD_S1:
                ans.append(str1[i1])
                i1 += 1
            else:
                ans.append(str2[i2])
                i2 += 1
        
        # Append remaining characters from str1 or str2
        while i1 < N1:
            ans.append(str1[i1])
            i1 += 1
        while i2 < N2:
            ans.append(str2[i2])
            i2 += 1
        
        return "".join(ans)