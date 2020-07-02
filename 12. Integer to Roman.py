class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, "C"), (90, "XC"),
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        result = ''
        for dig,mark in digits:
            count, num = divmod(num,dig)
            result += mark*count

        return result

so = Solution()
print(so.intToRoman(14))
