class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j]+grid[i][j-1]
        return grid[m-1][n-1]
Solution=Solution()
m = 3
n = 7
print(Solution.uniquePaths(m,n))

'''
Time Complexity: 
O(m×n) (since each cell is computed once)
Space Complexity: 
O(m×n) (due to the 2D DP table)
'''