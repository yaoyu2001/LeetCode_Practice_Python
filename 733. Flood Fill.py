import collections
class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if image[sr][sc] == newColor: return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r - 1 >= 0:
                    dfs(r - 1, c)
                if r + 1 < row:
                    dfs(r + 1, c)
                if c - 1 >= 0:
                    dfs(r, c - 1)
                if c + 1 < col:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image


class Solution2:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if image[sr][sc] == newColor:
            return image

        def bfs(image: [[int]], sr: int, sc: int, newColor: int):

            q = collections.deque()

            q.append([sr,sc])

            dir = [[-1,0],[1,0],[0,-1],[0,1]]

            while q:
                temp = q.popleft()
                r, c = temp[0], temp[1]
                image[r][c] = newColor
                for item in dir:
                    new_r = r + item[0]
                    new_c = c + item[1]
                    if 0 <= new_r < row and 0 <= new_c < col and image[new_r][new_c] == color:
                        q.append([new_r, new_c])

        bfs(image, sr, sc, newColor)
        return image

so2 = Solution2()

image = [[1,1,1],[1,1,0],[1,0,1]]
print(so2.floodFill(image, 1, 1, 2))


