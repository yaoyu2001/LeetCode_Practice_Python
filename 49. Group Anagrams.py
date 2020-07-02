import collections
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:

        ans = collections.defaultdict(list)

        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

so = Solution()
print(so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

class Solution2:
    def groupAnagrams(self, strs: [str]) -> [[str]]:

        ans = collections.defaultdict(list)
        count = [0]*26
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()