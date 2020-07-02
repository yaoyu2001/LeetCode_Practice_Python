# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        nonlocal counter
        def inorder(node, counter,k):
            if not node:
                return
            inorder(node.left, counter,k)
            if counter == k:
                return node.val
            counter += 1
            inorder(node.right, counter,k)


        counter = 0
        return inorder(root, counter, k)
