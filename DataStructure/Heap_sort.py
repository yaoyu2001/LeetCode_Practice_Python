# Use an array to indicate a heap because heap is a completely binary tree.
# parent = (i-1)/2 c1 = 2i + 1 c2 = 2i + 2 i = current node
# https://www.youtube.com/watch?v=j-DqQcNPGbE

def swap(tree, i, j):
    temp = tree[i]
    tree[i] = tree[j]
    tree[j] = temp

def heapify(tree:list,n,i):
    if i >= n: return
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max = i
    # Compare value of max to c1 and c2
    if c1 < n and tree[c1] > tree [max]:
        max = c1
    if c2 < n and tree[c2] > tree [max]:
        max = c2
    if max != i:
        swap (tree, max, i)
        heapify(tree, n, max)

tree = [4,10,3,5,1,2]
n = 6

heapify(tree,n,0)
print(tree)

# 20:12 in video, if nodes are inordered, heapify from the parent node of last node
def build_heap(tree:list, n:int):
    last_node = n - 1
    parent = last_node//2 - 1
    for i in range(parent,-1,-1):
        heapify(tree, n, i)

tree2 = [2,5,3,1,10,4]
n = 6
# heapify(tree2,n,0)
# print(tree2)
# build_heap(tree2,n)
# print(tree2)

# 25:30 heap sort, because the first node will always has the biggest value, we can push it and cut the last node to get an ordered list
def heap_sort(tree, n):
    build_heap(tree, n)
    for i in range(n -1, -1, -1):
        swap(tree, i, 0)
        # heapify "i" to "cut" the last node
        heapify(tree, i, 0)
        print(tree[i])
heap_sort(tree2,n)