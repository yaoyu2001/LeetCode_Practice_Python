# Definition for a binary tree node.
# https://www.youtube.com/watch?v=yH4nZe-5wDM&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=5
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def flattenTree(self, node):

        # Handle the null scenario
        if not node:
            return None

        # For a leaf node, we simply return the
        # node as is.
        if not node.left and not node.right:
            return node

        # Recursively flatten the left subtree
        leftTail = self.flattenTree(node.left)

        # Recursively flatten the right subtree
        rightTail = self.flattenTree(node.right)

        # If there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side
        # anymore.
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        # We need to return the "rightmost" node after we are
        # done wiring the new connections.
        return rightTail if rightTail else leftTail

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.flattenTree(root)


a = TreeNode(1)

b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
# g = TreeNode(10)

a.left =b
a.right = e
b.left = c
b.right = d
e.right = f
# d.right = g

so = Solution()
print(so.flatten(a))
