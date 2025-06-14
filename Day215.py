# Maximum Difference by rampping  a digit

class Solution:
    def minMaxDifference(self, num):
        INF = 10 ** 20

        mx = 0
        mn = INF 

        snum = str(num)
        for start in range(0, 10):
            for end in range(0,10):
                if start != end:
                    x = int(snum.replace(str(start), str(end)))

                    mx = max(x, mx)
                    mn = min(x, mn)
        return mx - mn
    