# Count Number of Powerful Integers

class Solution:
    def numberOfPowerfulInt(self, start, finish, limit, s):
        def f(x):
            xs = str(x)
            D = len(xs)
            L = len(s)

            total = 0
            if D == L:
                if int(xs) >= int(s):
                    total += 1
            elif D > L:
                    prefix = xs[:D-L]
                    suffix = xs[D-L:]
                    for index, p in enumerate(prefix):
                        p = int(p)
                        if p > limit:
                            over = True
                            total += pow(limit + 1, len(prefix) - index)
                            break
                        total += min(limit + 1, p) * pow(limit + 1, len(prefix) - index - 1)
                    else:
                        if int(suffix) >= int(s):
                            total += 1
            return total

        return f(finish) - f(start - 1)