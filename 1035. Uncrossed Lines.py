class Solution:
    def maxUncrossedLines(self, A: [int], B: [int]) -> int:

        if not A or not B or len(A) == 0 or len(B) == 0:
            return 0

        len_a, len_b = len(A), len(B)

        dp = [[0 for i in range(len_b + 1)] for j in range(len_a + 1)]

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len_a][len_b]



