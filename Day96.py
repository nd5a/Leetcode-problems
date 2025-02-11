# Remove all Occurences of a Substring

class Solution:
    def removeOccurrences(self, s, part):
        while part in s:
            index = s.index(part)
            s = s[:index] + s[index + len(part):]
        return s