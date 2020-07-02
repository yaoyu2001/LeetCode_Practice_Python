class Solution:
    def countBits(self, num: int) -> [int]:
        def popcount(x):
            count = 0
            while x != 0:
                x &= x - 1
                print(x)

                count += 1
            return count

        ans = []

        for i in range(num + 1):
            ans.append(popcount(i))

        return ans

    def popcount(self, x):
        count = 0
        while x != 0:
            x &= x - 1
            # print(x)

            count += 1
        return count

so = Solution()

print(so.popcount(4))

a = 1
# a += 1 * 2
a &= a-1
print(a)