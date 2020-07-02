# Definition for a binary tree node.
class BianryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

a = BianryTreeNode(8)
b = BianryTreeNode(3)
c = BianryTreeNode(10)
d = BianryTreeNode(1)
e = BianryTreeNode(6)
f = BianryTreeNode(15)
g = BianryTreeNode(5)
h = BianryTreeNode(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
f.right = h


so = Solution()
print(so.diameterOfBinaryTree(a))