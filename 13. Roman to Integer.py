class Solution:
    def romanToInt(self, s: str) -> int:

        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 0 or s is None:
            return 0

        res = dic[s[0]]

        for i in range(1, len(s)):
            if dic[s[i]] > dic[s[i - 1]]:
                res += dic[s[i]] - 2 * dic[s[i - 1]]
            else:
                res += dic[s[i]]
        return res

s = "CMXCVIII"

so = Solution()
print(so.romanToInt(s))