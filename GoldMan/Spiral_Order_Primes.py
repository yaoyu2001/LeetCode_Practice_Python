memo = set()
def is_prime_1(num):
    if num in memo:
        return True
    if num < 2:
        return False
    if num == 2:
        return True

    for i in range (2, int(num**0.5)):
        if num % i == 0:
            return False
    memo.add(num)
    return True


def spiralOrder(matrix):
    if not matrix: return []
    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in matrix]
    ans = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    for _ in range(R * C):
        if is_prime_1(matrix[r][c]):
            ans.append(matrix[r][c])
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return ans


def matrix_1(m):
    result = []
    while m:
        for i in m[0]:
            if is_prime_1(i):
                result.append(i)

        m.pop(0)
        print("*m")
        print(*m)
        print("zip")
        print(list(zip(*m)))
        m = list(zip(*m))[::-1]
    return result


matrix = [[7,7,3,8,1],[13,5,4,5,2],[9,2,12,3,9],[6,12,1,11,41]]

print(spiralOrder(matrix))
print(matrix_1(matrix))