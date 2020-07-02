class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for cur in range(1, amount + 1):
            for c in coins:
                if cur - c >= 0 and dp[cur - c] != -1:
                    if dp[cur] == -1 or dp[cur - c] + 1 < dp[cur]:
                        dp[cur] = dp[cur - c] + 1

        return dp[amount]