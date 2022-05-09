class Solution:
    def solve(self, N, K, A):
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                if A[i] + A[j] <= K:
                    ans += 1
        
        return ans
N = 5
K = 2
A = [5, 2, 4, 3, 5]