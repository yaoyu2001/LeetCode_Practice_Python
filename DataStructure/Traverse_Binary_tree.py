from LeetCode_Python.LeetCode_Practice_Python.DataStructure.BinaryTreeNode import BianryTreeNode
from collections import deque
a = BianryTreeNode(1)
b = BianryTreeNode(2)
c = BianryTreeNode(3)
# d = BianryTreeNode(4)
# e = BianryTreeNode(5)
# f = BianryTreeNode(6)
# g = BianryTreeNode(7)
a.left = b
a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g

def PreOrder(root):
    if root!= None:
        print(root.data)
        PreOrder(root.left)
        PreOrder(root.right)

def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.data)
        InOrder(root.right)

def PostOrder(root):
    if root != None:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data)

def PreOrder_Stack(root):
    if root == None: return None
    S = list()
    while True:
        while root!=None:
            print(root.data)
            S.append(root)
            root = root.left
        if not S:
            break
        root = S.pop()
        root = root.right

def InOrder_Stack(root):
    if root == None: return None
    S = list()
    while True:
        while root!= None:

            S.append(root)
            root = root.left
        if not S:
            break
        root = S.pop()
        print(root.data)
        root = root.right

def postorderTraversal(root):
    res = list()
    if root == None: return res
    s = list()
    s.append(root)
    prev = None
    while s:
        current = s[len(s) -1]
        if prev == None or prev.left == current or prev.right == current:
        # traverse from top to bottom, and if curr has left child or right child
        # push into the stack; otherwise, pop out.
            if current.left:
                s.append(current.left)
            elif current.right:
                s.append(current.right)
        elif current.left == prev:
            if current.right:
                s.append(current.right)
        else:
            res.append(current.data)
            s.pop()
        prev = current

    return res

# Level traverse
def LevelOrder(root):
    q = deque()
    temp = None
    if root == None: return None
    q.append(root)
    while q:
        temp = q.popleft()

        print(temp.data)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)




# PreOrder_Stack(a)

print(postorderTraversal(a))
LevelOrder(a)