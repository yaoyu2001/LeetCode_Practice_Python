import copy
class Solution:
    def generate(self, rowIndex: int) -> [int]:
        res = [1, 1]
        triangle = [[1], [1, 1]]

        if rowIndex == 0:
            return []
        elif rowIndex == 1:
            return triangle[:1]
        else:
            count = 1
            while rowIndex - count > 1:
                for i in range(1, count + 1):
                    res.append(res[i - 1] + res[i])
                res.append(1)
                res = res[count:]
                count += 1

                triangle.append(copy.deepcopy(res))

            return triangle


so = Solution()
print(so.generate(5))