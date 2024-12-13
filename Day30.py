class Solution:
    def canChange(self, start: str, target: str) -> bool:
        N = len(start)
        if start.count("L") != target.count("L"):
            return False
        if start.count("R") != target.count("R"):
            return False


        def check(start, target, correct, other):
            left = []
            for index, c in enumerate(target):
                if c == correct:
                        left.append(index)

            sindex = 0
            for lindex in left:
                sindex = max(sindex, lindex)

                while sindex < N and start[sindex] != correct:
                    if start[sindex] == other or target[sindex] == other:
                        return False         
                    sindex += 1
                
                if sindex == N:
                    return False
                
                assert(start[sindex] == correct)
                sindex += 1
            return True

        return check(start, target, "L", "R") and check(start[::-1], target[::-1], "R", "L")