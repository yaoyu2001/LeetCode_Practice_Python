import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = collections.Counter(s)
        max_length = 0
        flag = 0

        for item in dic.values():
            if item % 2 == 0:
                max_length += item
            else:
                max_length += item - 1
                flag = 1
        return max_length+flag
so = Solution()
print(so.longestPalindrome("aaa"))