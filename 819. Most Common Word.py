import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        banset = set(banned)

        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        paragraph = paragraph.lower().split()
        count = collections.Counter(paragraph)

        ans = ''
        best = 0
        for word in count:
            if count[word] > best and word not in banset:
                ans = word
                best = count[word]
        return ans

par = "a, a, a, a, b,b,b,c, c"
so = Solution()

print(so.mostCommonWord(par,["a"]))