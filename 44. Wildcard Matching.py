# https://www.youtube.com/watch?v=3ZDZ-N0EPV0

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        p = self.remove_duplicate(p)
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]

        dp[0][0] = True
        if len(p) > 0 and p[0] == "*":
            dp[0][1] = True

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j - 1] == "?" or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][
                        j]  # dp[i][j-1] when "*" represent 0 and dp[i-1][j] when it represent none
        return dp[len(s)][len(p)]

    def remove_duplicate(self, p):

        # del duplicate *
        if p == "":
            return p

        p1 = [p[0], ]
        for item in p[1:]:
            if p1[-1] != "*" or p1[-1] == "*" and item != "*":
                p1.append(item)

        return ''.join(p1)

s = "adceb"
p = "*a*b"

s1 = "aa"
p1 = "a"
p2 = "*"

s3 = "acdcb"
p3 = "a*c?b"


s4 = "aaaa"
p4 = "***a"
so = Solution()
print(so.isMatch(s4,p4))


