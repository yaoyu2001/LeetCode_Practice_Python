import collections


class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rot = collections.deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rot.append((i, j, 0))

        res = 0
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while rot:
            i, j, res = rot.popleft()

            for x_, y_ in d:
                x = i + x_
                y = j + y_
                if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                    grid[x][y] = 2
                    rot.append((x, y, res+1))
        if any(1 in row for row in grid):
            return -1

        return res


s = Solution()

org = [[2,1,1],[1,1,0],[0,1,1]]

print(s.orangesRotting(org))