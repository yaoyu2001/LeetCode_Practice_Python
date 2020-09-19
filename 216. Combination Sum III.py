# Backtrack
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        res = []

        def backtrack(goal, comb, next_start):
            if goal == n and len(comb) == k:
                res.append(list(comb))
                return
            elif goal > n or len(comb) == k:
                return
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(goal + i + 1, comb, i + 1)
                comb.pop()

        backtrack(0, [], 0)

        return res

so = Solution()
print(so.combinationSum3(3, 9))