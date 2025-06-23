# Sum of k-Mirror Numbers

class Solution:
    def kMirror(self, k, n):
        ans = []
        current = 1
        def go(x):
            a = []

            while x > 0:
                a.append(x % k)
                x //= k

            return a[::-1]
            
        def conv(now):
            t = 0
            for x in now:
                t *= k
                t += x
            return str(t)
        
        while True:
            now = go(current)

            nowMiddle = now + now[:-1][::-1]
            c = conv(nowMiddle)
            if c == c[::-1]:
                if len(ans) == n and int(c) > ans[-1]:
                    break
                ans.append(int(c))
                ans.sort()
                ans = ans[:n]
            
            if len(ans) < n:
                nowDouble = now + now[::-1]
                c = conv(nowDouble)
                if c == c[::-1]:
                    ans.append(int(c))
                    ans.sort()
                    ans = ans[:n]
            current += 1
        return sum(ans)