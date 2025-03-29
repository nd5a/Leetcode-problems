# Apply Operations to Maximize Score


MAX = 100005
prime = [True] * MAX
factors = [0] * MAX

prime[0] = prime[1] = False

for f in range(2, MAX):
    if prime[f]:
        factors[f] = 1
        s = f + f

        while s < MAX:
            factors[s] += 1
            prime[s] = False
            s += f

class Solution:
    def maximumScore(self, nums, k):
        N = len(nums)
        MOD = 10 ** 9 + 7
        INF = 10 ** 20
        MOD = 10 ** 9 +7
        #prime sieve of Erashenes

        p = [factors[x] for x in nums]

        left = [0] * N
        stack = [(-1, INF)]

        for index, x in enumerate(p):
            while stack[-1][1] < x:
                stack.pop()
            
            left[index] = index - stack[-1][0]
            stack.append((index, x))

        right = [0] * N
        stack = [(-1, INF)]
        for index, x in enumerate(p[::-1]):
            while stack[-1][1] <= x:
                stack.pop()
            
            right[index] = index - stack[-1][0]
            stack.append((index, x))
        right.reverse()

        ans = []
        for x, L, R in zip(nums, left, right):
            ans.append((x, L * R))
        ans.sort(reverse = True)

        score = 1
        for x, c in ans:
            to_use = min(c, k)
            score *= pow(x, to_use, MOD)
            score %= MOD
            k -= to_use

            
        return score % MOD