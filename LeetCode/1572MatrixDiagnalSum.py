class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        principal = 0
        secondary = 0
        
        for i in range(0, n):
            principal += mat[i][i]
            secondary += mat[i][n - i - 1]
            
        if n % 2 == 1: secondary -= mat[n // 2][n // 2]
        
        return principal + secondary