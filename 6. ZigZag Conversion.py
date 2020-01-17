class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ret = []
        n = len(s)
        cycleLen = 2 * numRows - 2
        for i in range(numRows):
            for j in range(0, n-i, cycleLen):
                ret.append(s[j+i])
                if i !=0 and i != numRows-1 and j + cycleLen - i < n:
                    ret.append(s[j+cycleLen-i])
        return "".join(ret)

s = "12345678"
n = 4

So = Solution()

print(So.convert(s, n))