# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:

        n = len(preorder)

        def pre_order(lower = float('-inf'), high = float('inf')):
            nonlocal idx
            if idx == n:
                return None
            val = preorder[idx]
            if val<lower or val>high:
                return None

            idx += 1
            root = TreeNode(val)
            root.left = preorder(lower, val)
            root.right = preorder(val, high)
            return root

        idx = 0
        return preorder()
