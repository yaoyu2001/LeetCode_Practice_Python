class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:

        row, col = len(triangle), len(triangle[len(triangle) - 1])

        dp = [[float('inf') for i in range(col)] for j in range(row)]
        dp[0][0] = triangle[0][0]

        print(dp)
        for i in range(1, row):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        print(dp)
        return min(dp[row - 1])


so = Solution()
print(so.minimumTotal([
     [-1],
    [3,2],
   [-3,1,-1]

]))