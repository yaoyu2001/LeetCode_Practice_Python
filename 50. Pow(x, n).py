class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:return 1
        if n ==1 :return x

        """Use -(power+1) to avoid MIN_VALUE case """
        if n < 0: return 1/(x*self.myPow(x, -(n+1)))
        res = 1

        while n>1:
            if n%2 ==1:
                res *=x
            x = x*x
            n = n//2
        res *= x
        return res