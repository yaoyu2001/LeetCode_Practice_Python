class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0 for i in range(len(dungeon[0]) + 1)]