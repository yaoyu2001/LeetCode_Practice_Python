import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1, cnt2 = map(collections.Counter, (s, t))
        print(cnt1 - cnt2)
        return sum((cnt1 - cnt2).values())

so = Solution()

print(so.minSteps("leetcode", "practice"))