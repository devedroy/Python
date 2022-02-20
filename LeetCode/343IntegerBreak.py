class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1 : 1}

        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num == n else num