# Delete Characters to Make Fancy String

class Solution:
    def makeFancyString(self, s: str) -> str:
        current = []
        for c in s:
            current.append(c)
            if len(current) >= 3 and current[-3] == current[-2] == current[-1]:
                current.pop()
        return "".join(current)