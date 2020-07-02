class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        row,col = len(grid), len(grid[0])

        dp = [[0 for i in range(col)] for j in range(row)]

        # print(dp)
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j !=0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif i !=0 and j ==0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j-1])

        return dp[row-1][col-1]
        # print(dp)

so = Solution()

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(so.minPathSum(grid))