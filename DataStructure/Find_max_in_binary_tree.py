from LeetCode_Python.LeetCode_Practice_Python.DataStructure.BinaryTreeNode import BianryTreeNode

a = BianryTreeNode(1)
b = BianryTreeNode(2)
c = BianryTreeNode(3)
d = BianryTreeNode(4)
e = BianryTreeNode(5)
f = BianryTreeNode(6)
g = BianryTreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

def find_max(root):
    root_val = float("-inf")
    left= float("-inf")
    right= float("-inf")
    max= float("-inf")

    if root:
        root_val = root.data
        left = find_max(root.left)
        right = find_max(root.right)
        if left > right:
            max = left
        else:
            max = right
        if root_val>max:
            max = root_val
    return max

print(find_max(a))