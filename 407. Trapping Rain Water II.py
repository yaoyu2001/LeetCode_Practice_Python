# https://www.youtube.com/watch?v=GL1HvaYKE40&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=10&t=13494s
from queue import PriorityQueue as PQueue

class Cell:
    def __init__(self,x, y, h):
        self.x = x
        self.y = y
        self.h = h
    def __lt__(self, other):
        if self.h <= other.h:
            return True
        else:
            return False


class Solution:
    def trapRainWater(self, heightMap: [[int]]) -> int:
        # if row or col < 3, return 0
        row, col = len(heightMap), len(heightMap[0])
        if row < 3 or col < 3:
            return 0
        # A matrix which has same size of given map to indicate whether a cell is visited
        mark = [[0 for i in range(col)] for j in range(row)]
        # Use a Priority Queue to search
        # First push all sides of matrix to pq
        pq = PQueue()

        for i in range(row):
            pq.put(Cell(i,0,heightMap[i][0]))
            mark[i][0] = 1
            pq.put(Cell(i, col -1 , heightMap[i][col-1]))
            mark[i][col-1] = 1

        for j in range(1, col-1):
            pq.put(Cell(0, j, heightMap[0][j]))
            mark[0][j] = 1
            pq.put(Cell(row-1, j, heightMap[row-1][j]))
            mark[row-1][j] = 1

        # print(mark)
        # while pq:
        #
        #     temp = pq.get()
        #     print(temp.x, temp.y, temp.h)

        dir = [[0,-1],[0,1],[-1,0],[1,0]]
        res = 0

        while not pq.empty():
            cur = pq.get()
            # print(cur.x, cur.y, cur.h)
            for item in dir:
                new_x = cur.x + item[0]
                new_y = cur.y + item[1]
                # print(f"new_x :  {new_x} new_y: {new_y}")
                if new_x < 0 or new_x>=row or new_y<0 or new_y>= col or mark[new_x][new_y]==1:
                    # print("continue")
                    continue
                if cur.h > heightMap[new_x][new_y]:
                    # print("res+ ", cur.h - heightMap[new_x][new_y])
                    res += cur.h - heightMap[new_x][new_y]
                    heightMap[new_x][new_y] = cur.h
                pq.put(Cell(new_x, new_y, heightMap[new_x][new_y]))
                mark[new_x][new_y] = 1





        return res




so = Solution()
print(so.trapRainWater([
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]))



