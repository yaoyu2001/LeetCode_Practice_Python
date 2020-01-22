# https://www.youtube.com/watch?v=e_bK-dgPvfM
# Segment tree, use an array to show a segment tree

MAX_LEN = 1000 # define max value of arr


def build_tree(arr, tree, node, start, end):
    if start == end:
        """If start == end that means the current node is leaves node, now let current node = value in arr"""
        tree[node] = arr[start]
    else:
        mid = (start + end)//2  # mid number in tree to make sure the range of left part and right part in a tree
        left_node = 2*node + 1  # Index of left child of current node
        right_node = 2*node + 2  # Index of right child of current node
        build_tree(arr, tree, left_node, start, mid)  # Recursion to build left part of tree
        build_tree(arr, tree, right_node, mid + 1, end)  # Recursion to build right part of tree

        tree[node] = tree[left_node] + tree[right_node]  # current node's value = sum of it's child nodes


def update_tree(arr, tree, node, start, end , index ,value):
    if start == end:
        arr[index] = value
        tree[node] = value
    else:
        mid = (start + end)//2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        if start <= index <= mid:
            update_tree(arr, tree, left_node, start, mid, index,value)
        elif mid < index <= end:
            update_tree(arr, tree, right_node, mid+1, end, index, value)

        tree[node] = tree[left_node] + tree[right_node]

def query_tree(arr, tree, node, start, end ,L, R):
    """According to range (L,R) compare with mid, got sum part"""
    if L > end or R < start:
        return 0
    elif start == end:
        return tree[node]
    elif L<= start and end <=R:
        return tree[node]
    else:
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        sum_left = query_tree(arr, tree, left_node, start, mid ,L, R)
        sum_right = query_tree(arr, tree, right_node, mid + 1, end ,L, R)
        return sum_left + sum_right


def main():
    arr = [1, 3, 5,7,9,11]
    size = 6
    # tree = [0] * MAX_LEN
    tree = [0]*20

    build_tree(arr, tree, 0, 0, size-1)
    print(tree)
    update_tree(arr, tree, 0, 0, size-1 , 4 ,6)
    print(tree)
    print(query_tree(arr, tree, 0, 0, size-1 ,2, 5))
if __name__ == '__main__':
    main()



