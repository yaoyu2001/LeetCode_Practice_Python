# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS Preorder
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        # A container to save nodes in every level
        levels =[]
        if not root:
            return levels

        # Pre order traversal every levels
        # Parameters current node and current level
        def pre_order(node, level):
            # len(levels) == level that means we need more node container
            # number of "levels" must always bigger 1 than number "level"
            if len(levels) == level:
                levels.append([])
                # current level will always be levels[level]

            # Append current node to current level
            levels[level].appedn(node.val)

            # Recursive nodes in next level
            if node.left:
                pre_order(node.left, level + 1)
            if node.right:
                pre_order(node.right, level + 1)

        pre_order(root, 0)
        # Need reserved result
        return levels[::-1]


