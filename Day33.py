class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)

        current = None
        streak = 0 

        f = collections.defaultdict(collections.Counter)

        def process(c, streak):
            s = streak
            count = 1

            while s > 0:
                f[c][s] += count
                count += 1
                s -= 1
        
        for c in s:
            if c == current:
                streak += 1
            else:
                process(current, streak)

                current = c
                streak = 1
        else:
            process(current, streak)
        
        best = -1
        for c in f.keys():
            for L in f[c]:
                if f[c][L] >= 3:
                    best = max(best, L)
        return best