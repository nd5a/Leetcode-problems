# Pascal's Triangle

class Solution:
    def generate(self, numRows: int):
        """
        1
        1 1
        1 2 1
        1 3 3 1
        ...
        """

        ans = [[1]]
        for i in range(1, numRows):
            ans.append([])

            for j in range(i + 1):
                r = 0
                if j < i:
                    r += ans[i-1][j]
                if j >= 1:
                    r += ans[i - 1][j - 1]
                ans[i].append(r)
        return ans 