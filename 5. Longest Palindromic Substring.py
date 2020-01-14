# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000
# DP
class LongestPalindrome:
    def longestPalindrome( self, s: str) -> str:
        if not s:
            return ''
        dp = [[True if i == j else False for i, _ in enumerate(s)] for j, _ in enumerate(s)]
        maxLen = 1
        maxPalindrome = s[0]

        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxLen = 2
                maxPalindrome = s[i:i + 2]

        for k in range(2, len(s)):
            for i in range(0, len(s) - k):
                j = i + k
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        maxPalindrome = s[i:j + 1]

        return maxPalindrome


s = LongestPalindrome()

print(s.longestPalindrome("a"))


# https://www.youtube.com/watch?v=g3R-pjUNa3k
class LongestPalindrome2:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0

        def getLen(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(len(s)):
            cur = max(getLen(i, i), getLen(i, i + 1))
            if cur > max_len:
                max_len = cur
                start = i - (cur - 1) // 2
        return s[start:start + max_len]

s2 = LongestPalindrome2()
input = "abcbca"

print(s2.longestPalindrome(input))