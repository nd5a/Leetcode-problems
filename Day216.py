# Max Difference You can get from changinh an Integer

class Solution:
    def maxDiff(self, num):
        INF = 10 ** 20

        mx = 0
        mn = INF

        snum = str(num)
        for start in range(0, 10):
            for end in range(0, 10):
                if start != end:
                    sx = snum.replace(str(start), str(end))
                    if sx[0] == "0":
                        continue
                    x = int(sx)

                    mx = max(x, mx)
                    mn = min(x, mn)
        return mx - mn