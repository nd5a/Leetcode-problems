# Find the K-th Character in String Game I

class Solution:
    def kthCharacter(self, k):
        s = ["a"]

        while len(s) < k:
            ns = []
            for c in s:
                ns.append(chr(ord(c) + 1))
            
            s.extend(ns)
        return s[k - 1]