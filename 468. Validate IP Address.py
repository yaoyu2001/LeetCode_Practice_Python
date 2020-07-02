class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validIPV4(IP)
        elif IP.count(':') == 7:
            return self.validIPV6(IP)
        else:
            return "Neither"

    def validIPV4(self, IP:str) -> str:
        nums = IP.split('.')
        for n in nums:
            if len(n) == 0 or len(n) > 3:
                return "Neither"

            if n[0] == '0' and len(n) != 1 or not n.isdigit() or int(n) > 255:
                return "Neither"

        return "IPv4"



    def validIPV6(self, IP: str) -> str:
        hexdigits = '0123456789abcdefABCDEF'
        nums = IP.split(":")
        for n in nums:
            if len(n) == 0 or len(n) > 4 or not all(c in hexdigits for c in n):
                return "Neither"

        return "IPv6"

so = Solution()

print(so.validIPAddress(
"01.01.01.01"))
