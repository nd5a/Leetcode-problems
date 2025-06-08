# Lexicographical Numbers

class Solution:
    def lexicalOrder(self, n):
        ans = []
        def recurse(current):
            ans.append(current)
            for i in range(0, 10):
                if current * 10 + i <= n:
                    recurse(current * 10 + i)
        
        for i in range(1, 10):
            if i <= n:
                recurse(i)
        return ans