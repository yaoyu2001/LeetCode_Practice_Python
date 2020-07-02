import math
class Solution(object):
    def numSquares(self, n):
        squares = [i**2 for i in range(int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n+1)

        dp[0] = 0

        for i in range(n+1):
            for s in squares:
                if i < s:
                    break
                dp[i] = min(dp[i] , dp[i-s] + 1)

        return dp[-1]

so = Solution()
print(so.numSquares(12))
