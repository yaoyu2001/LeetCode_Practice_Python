class Solution:
    def exist(self, board: [[str]], word: str) -> bool:

        self.row,self.col = len(board), len(board[0])
        self.board = board

        for r in range(self.row):
            for c in range(self.col):
                if self.backtrack(r, c, word):
                    return True
        # No match after all exploration
        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True

        # Check current state, if we need to backtrack
        if row < 0 or row > self.row - 1 or col < 0 or col > self.col + 1 \
            or self.board[row][col] != suffix[0]:
            return False

        ret = False # Mark if find word
        # Mark cells in searching,
        self.board[row][col] = '#'

        for r_offset, c_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + r_offset, col + c_offset, suffix[1:])

            if ret:
                break

        self.board[row][col] = suffix[0]

        return ret
