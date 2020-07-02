# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def dfs(node, depth, val, find=False):
            if not node:
                return

            if node.val == val:
                return depth

            l = dfs(node.left, depth + 1, val, find)
            r = dfs(node.right, depth + 1, val, find)

            return l or r

        def same_parent(node, x, y):
            if not node:
                return False
            if node.left and node.right:
                if node.left.val == x and node.right.val == y:
                    return True
                if node.left.val == y and node.right.val == x:
                    return True

            l = same_parent(node.left, x, y)
            r = same_parent(node.right, x, y)

            return l or r

        # print(dfs(root, 0, x))
        # print(dfs(root, 0, y))
        print(same_parent(root, x, y))
        return dfs(root, 0, x) == dfs(root, 0, y) and not same_parent(root, x, y)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)


a.right = b
b.left = c
c.left = d
d.right = f
b.right = e

so = Solution()
# so.isCousins(a, 4, 3)
print(so.isCousins(a, 5, 3))