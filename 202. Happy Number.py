class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            sum = 0
            while n > 0:
                digit = n%10
                sum += digit**2

            return sum

        seen = set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n==1