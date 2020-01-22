# Build a binary
n = 5
A = [0] * n

def binary(n:int):

    if n < 1:
        print(A)
    else:
        A[n -1] = 0
        binary(n-1)
        A[n -1] = 1
        binary(n-1)

binary(5)