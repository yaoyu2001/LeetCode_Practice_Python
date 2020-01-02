import heapq

def matrixGame(matrix):
    row = len(matrix)
    col = len(matrix[0])

    pqueue_max = list()

    for j in range(col):
        col_max = float("-inf")
        for i in range(row):
            col_max = max(col_max, matrix[i][j])

        heapq.heappush(pqueue_max, -col_max)

    tom = 0
    jerry = 0
    tomTurn = True
    while pqueue_max:
        if tomTurn:
            temp_tom = -heapq.heappop(pqueue_max)
            print(f"Tom pick {temp_tom}")
            tom += temp_tom
            print(f"Tom now {tom}")

        else:
            temp_jerry = -heapq.heappop(pqueue_max)
            print(f"jerry pick {temp_jerry}")
            jerry += temp_jerry
            print(f"jerry now {jerry}")


        tomTurn = not tomTurn
        print(tomTurn)
    return tom - jerry


matrix = [[5,7,6,2,8,4,4,8],
          [2,5,4,5,9,8,4,2],
          [5,4,3,9,8,3,3,4],
          [4,9,3,4,6,7,4,9],
          [2,4,6,2,9,2,4,2]]

matrix2 =[[3,7,5,3,4,5], [4,5,2,6,5,4], [7,4,9,7,8,3]]

print(matrixGame(matrix))
print(matrixGame(matrix2))
# pqueue = list()
# nums= [2,34,1,5,15,1,52,56,12]
# for i in nums:
#     heapq.heappush(pqueue,-i)
# print(pqueue)
#
# while (len(pqueue) > 0):
#     print(-heapq.heappop(pqueue))
#
# for i in range(本群人数):
#     刚哥最帅 += 1