class Solution:
    def findJudge(self, N: int, trust: [[int]]) -> int:

        if len(trust) < N - 1: return -1

        trust_check = [0] * (N + 1)

        for a, b in trust:
            trust_check[a] -= 1
            trust_check[b] += 1

        for no, item in enumerate(trust_check[1:], 1):
            if item == N - 1:
                return no

        return -1