class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.rows = [0] * self.size
        self.cols = [0] * self.size
        self.d1 = 0 # diagonal
        self.d2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            res = self.makeMove(row, col, 1)
        else:
            res = self.makeMove(row, col, -1)

        if res == -1:
            return 2
        else:
            return res

    def makeMove(self, i, j, step):
       if self.rows[i] !=0 and self.cols[j]!=0:
           raise ValueError

       else:
            if i == j and i + j == self.size - 1:
                self.d1 += step
                self.d2 += step
            elif i == j:
                self.d1 += step
            elif i + j == self.size - 1:
                self.d2 += step
            self.rows[i] += step
            self.cols[j] += step

            if self.rows[i] == step * self.size or self.cols[j] == step * self.size or self.d1 == step * self.size or self.d2 == step * self.size:
                return step
            else:
                return 0

toe =TicTacToe(3)
print(toe.move(0, 0, 1))
print(toe.move(0, 2, 2))
print(toe.move(2, 2, 1))
print(toe.move(1, 1, 2))
print(toe.move(2, 0, 1))
print(toe.move(1, 0, 2))
print(toe.move(2, 1, 1))
#
# toe.move(0, 2, 2);
# toe.move(2, 2, 1);
#
# toe.move(1, 1, 2);
#
# toe.move(2, 0, 1);
#
# toe.move(1, 0, 2);
#
# toe.move(2, 1, 1)