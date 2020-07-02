# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum_ = 0
        self.cur = ""

        def dsf(node, cur):
            if node:
                cur = 10 * cur + node.val

                if not (node.left or node.right):
                    self.sum_ += int(cur)
                dsf(node.left, cur)
                dsf(node.right, cur)

        dsf(root, 0)
        return self.sum_


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.left = b
a.right = c

so = Solution()
print(so.sumNumbers(a))