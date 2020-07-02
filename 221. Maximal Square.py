class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:

        if len(matrix) != 0:
            dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]

        max_len = 0

        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    max_len = max(dp[i][j], max_len)

        return max_len * max_len