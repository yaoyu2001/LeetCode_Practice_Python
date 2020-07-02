class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1

        temp, bit = N, 1
        while temp:
            N = N^bit
            temp = temp >>1
            bit = bit<<1
        return N