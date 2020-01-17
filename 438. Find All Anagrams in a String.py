import collections
class Solution:

    def findAnagrams(self, s: str, p: str) -> [int]:
        ls, lp, res = len(s), len(p), []
        cp, cs = collections.Counter(p), collections.Counter(s[:len(p)-1])
        for i in range(len(s) - len(p) + 1):
            first, last = s[i], s[i+lp-1]
            cs.update(last)
            if cp == cs:
                res.append(i)
            if cs[first] > 1:
                cs.subtract(first)
            else:
                # del cs[first]
                cs.pop(first)
        return res

s1 = "aaabab"
p1 = "aba"

s = Solution()
print(s.findAnagrams(s1, p1))