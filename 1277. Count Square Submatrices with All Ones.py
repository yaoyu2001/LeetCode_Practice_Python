class Solution:
    def countSquares(self, matrix: [[int]]) -> int:
        result = 0
        if matrix is None or len(matrix) == 0:
            return result

        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        result += 1
                    else:
                        cell_val = min(matrix[r-1][c-1], matrix[r-1][c],matrix[r][c-1]) + matrix[r][c]
                        result += cell_val
                        matrix[r][c] = cell_val
        return result

