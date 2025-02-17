# Letter till Possibilities

import collections
class Solution:
    def numTilePossibilities(self, tiles):
        f = collections.Counter(tiles)
        keys = f.keys()

        def to_keys(f):
            s = []
            for k in keys:
                s.append(f[k] * k)
            return "".join(s)
        
        def from_keys(s):
            return collections.Counter(s)
        
        def go(left, s):
            count = 1
            f = from_keys(s)

            for k in keys:
                if f[k] > 0:
                    f[k] -= 1
                    count += go(left - 1, to_keys(f))
                    f[k] += 1
            return count
        
        return go(len(tiles), to_keys(f)) - 1