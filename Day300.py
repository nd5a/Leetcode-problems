# Number of People Aware of a Secret

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)  
        dp[1] = 1  # On day 1, one person learns the secret
        
        share = 0  # number of people who can share the secret on current day
        
        for day in range(2, n + 1):
            # New people who can start sharing today
            share = (share + dp[day - delay]) % MOD if day - delay >= 1 else share
            # People who forget today should be removed
            share = (share - dp[day - forget]) % MOD if day - forget >= 1 else share
            dp[day] = share
        
        # Count people who still remember the secret at the end of day n
        ans = 0
        for day in range(n - forget + 1, n + 1):
            if day >= 1:
                ans = (ans + dp[day]) % MOD
        
        return ans
