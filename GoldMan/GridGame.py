
def gridGame(grid, k, rules):
    if not grid:
        return grid
    states = [grid]
    n = len(grid)
    m = len(grid[0])
    while k > 0:
        print(f"k  {k}")
        k -= 1
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                cnt = findNeighbor(grid, i, j)
                # print(i,j,cnt)
                if rules[cnt] == "alive":
                    res[i][j] = 1

        if res in states:
            i = states.index(res)

            states = states[i:]
            # print(k)
            # print((k+1) % len(states) - 1)
            # return res
            print(f"array now  {states} and k is {k}")
            print(f"target is {(k + 1) % len(res) - 1} {states[(k + 1) % len(res) - 1]}")
            return states[(k + 1) % len(states) - 1]
        else:
            states.append(res)
            print("Not find .. .")
            print(f"Res added {res}")
            # print(states)
            grid = res

    return grid


def findNeighbor(grid, row, col):
    neighbor = [[-1,1],[-1,0],[-1,-1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    cnt = 0
    for i in range(0,8):
        x = row + neighbor[i][0]
        y = col + neighbor[i][1]
        if 0 <= x < len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
            cnt += 1

    return cnt

grid = [[0,1,0,0], [0,0,0,0]]
states = [grid]
k = 2
# print(states)
rules = ["dead", "alive","dead","dead","dead","alive","dead","dead",'dead']

print(gridGame(grid,4,rules))

# def run(grid, rules):
#     res = []
#     for k in range(1,16):
#         print(f"K = {k}")
#         # temp = gridGame(grid, k, rules)
#         # if temp in res:
#         #     for c in gridGame(grid,k,rules):
#         #             print(c)
#         # else:
#         #     res.append(temp)
#         print(gridGame(grid,k,rules))
#
# run(grid,rules)

arry = '123456767'
num1 = 7
char = '6'


def test_remainder(arry, k, char):
    counter = 0
    res = []
    while k > 0:
        print(f"k  {k}")
        k -= 1
        print(counter, arry[counter])
        temp = arry[counter]
        counter += 1
        if char in res:
            print(f"k  {k} found")
            i = res.index(char)
            print(f"i  {i} {res}")
            res = res[i:]

            print(f"array  {res}")
            print(f"target {res[(k+1)%len(res) - 1]}")
            return
        else:
            print("Not find ...")
            res.append(temp)
            print(f"Res added {temp}")



# test_remainder(arry, num1,char)
