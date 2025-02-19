# The k-th Lexicographical String of All Happy Strings of Length n

class Solution:
    def getHappyString(self, N: int, k: int) -> str:
        k -= 1

        ans = []
        if k < pow(2, N - 1):
            ans.append(0)
        elif pow(2, N - 1) <= k < 2 * pow(2, N - 1):
            ans.append(1)
            k -= pow(2, N - 1)
        elif 2 * pow(2, N - 1) <= k < 3 * pow(2, N - 1):
            ans.append(2)
            k -= 2 * pow(2, N - 1)
        else:
            return ""
        
        # k is now binary number
        for offset in range(N - 2, -1, -1):
            x = int((1 << offset & k) > 0)

            current = 0
            if current == ans[-1]:
                current += 1
            
            if x == 1:
                current += 1
                if current == ans[-1]:
                    current +=1
            ans.append(current)
        
        return "".join("abc"[x] for x in ans)