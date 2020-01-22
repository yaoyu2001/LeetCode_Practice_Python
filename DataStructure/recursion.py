# Use recursion to solve hanoi tower
def hanoitower(n:int, a: str, c: str, b: str):
    if n == 1:
        """If only one plate, move it from a to c"""
        return print(f"More item 1 from peg {a} to top peg {c}")
    else:
        """Move n-1 plates from a to b, """
        hanoitower(n-1, a, b, c)
        print(f"More item  from peg {a} to top peg {c}")
        hanoitower(n-1, b, c, a)

# hanoitower(3,"A","C","B")

# Judge if an array is ordered
def checkorder(array:list, index:int):
    if len(array) == 1: return 1
    else:return 0 if array[index - 1]<=array[index-2] else checkorder(array[:-1],index - 1)


# print(checkorder([1,3,4],2))
n = 2
array = [1] * n
print(array)