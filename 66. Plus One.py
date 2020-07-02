class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        num = ""
        res = []
        for dig in digits:
            num += str(dig)
        for i in str(int(num) + 1):
            res.append(int(i))

        return res

so = Solution()

print(so.plusOne([1,2,3]))