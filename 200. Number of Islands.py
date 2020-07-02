import collections


class Solution:
    def numIslands(self, grid: [[str]]) -> int:

        self.mark = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.mark[i][j] == 0 and grid[i][j] == '1':
                    self.DFS(grid, self.mark, i, j)
                    island += 1
        return island

    def DFS(self, grid, mark, x, y):
        grid_step = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.mark[x][y] = 1
        for item in grid_step:
            new_x = x + item[0]
            new_y = y + item[1]

            if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
                continue
            if grid[new_x][new_y] == '1' and self.mark[new_x][new_y] == 0:
                self.DFS(grid, self.mark, new_x, new_y)

    def BFS(self, grid, mark, x, y):
        q = collections.deque()
        grid_step = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q.append([x, y])
        mark[x][y] = 1
        while q:
            temp = q.popleft()
            x = temp[0]
            y = temp[1]

            for item in grid_step:
                new_x = x + item[0]
                new_y = y + item[1]
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
                    continue
                if grid[new_x][new_y] == '1' and mark[new_x][new_y] == 0:
                    q.append([new_x, new_y])
                    mark[new_x][new_y] = 1


so = Solution()
arr = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
arr2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(so.numIslands(arr))
print(so.numIslands(arr2))

#
# mark = [[0 for i in range(4)] for j in range(4)]
# print(mark)
