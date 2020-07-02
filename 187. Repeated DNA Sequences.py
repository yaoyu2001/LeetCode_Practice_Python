class Solution:
    def findRepeatedDnaSequences(self, s: str) -> [str]:
        L = 10
        n = len(s)
        seen = set()
        result = []

        for start in range(n-L+1):
            temp = s[start:start+L]

            if temp in seen:
                result.append(temp)

            seen.add(temp)

        return result


so = Solution()

print(so.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
