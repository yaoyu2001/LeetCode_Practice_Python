#https://www.youtube.com/watch?v=eRBpfoWujQM

# In k-1 days : dp[j][k-1] , in 1 day: max_day = max(jobs[j+1]~ j[i])
class Solution:
    def minDifficulty(self, jobDifficulty: [int], d: int) -> int:
        n = len(jobDifficulty)
        if d>n:return -1
        dp = [[float("inf") for i in range(d+1)] for j in range(n+1)]

        dp[0][0] = 0
        for i in range(1, n+1):
            for k in range(1, d+1):
                md = 0
                """We need at least one job in a day, so j<=k-1 so range(i-1, k-2, -1)"""
                for j in range(i-1, k-2, -1):
                    md = max(md, jobDifficulty[j])
                    dp[i][k] = min(dp[i][k], dp[j][k-1] + md)

        return dp[n][d]

so = Solution()
input = [6,5,4,3,2,1]

print(so.minDifficulty(input,2))