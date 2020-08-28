# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        # Build a map to store idx of every node in inorder list
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        # A help function to build tree
        def helper(in_left, in_right):
            # No elements to construct tree
            if in_left > in_right:
                return None

            # pop a node from postorder list as root node
            val = postorder.pop()
            root = TreeNode(val)

            # Use root's idx of inorder list to splite list as left and right subtrees
            idx = idx_map[val]

            # Subtree recursion
            root.right = helper(idx + 1, in_right)
            root.left = helper(in_left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)

