class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m < 2 or n < 2:
            return 1

        dp = [[0 for i in range(m)] for j in range(n)]

        for i in range(1, m):
            dp[0][i] = 1

        for j in range(1, n):
            dp[j][0] = 1

        # print(dp)

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # print(dp)

        return dp[n - 1][m - 1]

so = Solution()
# so.uniquePaths(3,2)
print(so.uniquePaths(7, 3))