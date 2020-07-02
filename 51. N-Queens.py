import copy
class Solution:


    def solveNQueens(self, n: int) -> [[str]]:
        mark = [[0 for i in range(n)] for j in range(n)] #
        location = [["." for i in range(n)] for j in range(n)] # One possible solution
        result = []
        self.generate(0, n, location, mark, result)
        result_final = []
        for r in result:
            temp = []
            for item in r:
                temp.append("".join(item))
            print(temp)
            result_final.append(temp)
        return result_final

    def generate(self,k,n,location,mark,result):
        """Recursion and track back to generate the position of 'Q' """
        """k means recur to 'k' row which range from 0 to n-1, n means board length."""
        """location means a possible solution which formed with 'Q' and '.'"""
        """Mark means the area that a 'queen' can attack, which formed with 1 and 0, we only can put a 'queen' in 0 cell"""
        """If we have finished one recursion successfully, we can push that location to  """

        if k == n:
            """When we go to the last row, which means k == n, push result and return"""
            result.append(copy.deepcopy(location))
            return

        for i in range(n):
            """Try every col of a row"""
            if mark[k][i] == 0:
                """When current cell == 0, that means we can push a Q in this cell, but we still need temp mark to record current mark, so that we can back track to this codition"""
                temp_mark = copy.deepcopy(mark)
                """Now put Q"""
                location[k][i] = "Q"
                self.put_down_queen(k, i, mark)
                """Then we recursion put Q to next row"""
                self.generate(k+1, n, location, mark, result)
                """if this recursion not finished, track back condition, try next col cell"""
                mark = temp_mark
                location[k][i] = "."

    def put_down_queen(self, x, y, mark):

        dx = [-1,1,0,0,-1,-1,1,1]
        dy = [0,0,-1,1,-1,1,-1,1]
        mark[x][y] = 1

        for i in range(1,len(mark)):
            for j in range(0,8):
                new_x = x + i*dx[j]
                new_y = y + i*dy[j]

                if 0<= new_x<len(mark) and  0<= new_y<len(mark):
                    mark[new_x][new_y] = 1

so = Solution()

# so.solveNQueens(8)

print(so.solveNQueens(4))
