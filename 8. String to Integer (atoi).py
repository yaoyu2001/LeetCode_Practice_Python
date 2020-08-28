class Solution:
    def myAtoi(self, str: str) -> int:
        if str == '0' or len(str) == 0:
            return 0

        str_list = list(str.strip())
        if str == '0' or len(str_list) == 0:
            return 0
        sign = -1 if str_list[0] == "-" else 1
        start = 1 if str_list[0] == '-' or str_list[0] == '+' else 0
        sum = 0

        for i in range(start, len(str_list)):
            if str_list[i].isdigit():
                sum = sum * 10 + ord(str_list[i]) - ord('0')
            else:
                break

        return max(-2 ** 31, min(sign * sum, 2 ** 31 - 1))

