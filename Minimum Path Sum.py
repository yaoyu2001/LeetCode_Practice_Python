class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif i != 0 and j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
        return dp[len(grid) - 1][len(grid[0]) - 1]

so = Solution()

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(so.minPathSum(grid))