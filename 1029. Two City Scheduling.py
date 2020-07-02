class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        n = len(costs) // 2

        res = 0
        for i in range(n):
            res += costs[i][0] + costs[i + n][1]

        return res
