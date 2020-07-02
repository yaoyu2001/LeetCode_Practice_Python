class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # j = set(J)
        res = 0
        for item in S:
            if item in J:
                res += 1
        return res