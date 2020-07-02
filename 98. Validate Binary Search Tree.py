# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Method 1 recursion
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def isValidBST(root, min_val, max_val):
            if not root:
                return False
            if root.val <= min_val or root.val>=max_val:
                return False
            return isValidBST(root.left, min_val, root.val) and isValidBST(root.right, root.val, max_val)

        return isValidBST(root, float("-inf"), float("-inf"))


# Method 2 Inorder traversal
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        stack=[]
        inorder = float("-inf")

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:break
            root = stack.pop()
            if root.val<= inorder:return False
            inorder = root.val
            root = root.right
        return True


matrix = [[0 for i in range(4)] for j in range(3)]

print(matrix)



