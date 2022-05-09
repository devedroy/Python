class Solution:
    def solve(self, N, K, A):
        # write your code here
        if K == 1:
            return 0
        if K == N:
            return 1
        if K > N:
            return 0
        dp = [[0 for i in range(K + 1)] for j in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, K + 1):
                if j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[N][K] % 1000000007
        

N = 4
K = 2
A = [3, 10, 5, 20]