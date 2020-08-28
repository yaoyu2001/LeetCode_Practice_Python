class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        res = [1, 1]

        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return res
        else:
            count = 0
            while rowIndex - count > 1:
                for i in range(1, count + 2):
                    res.append(res[i - 1] + res[i])
                res.append(1)
                count += 1
                res = res[count:]

            return res


so = Solution()
print(so.getRow(4))
