# Given a complete binary tree, count the number of nodes.
#
# Note:
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Example:
#
# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# Output: 6

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0

class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        height = 0
        cur = root
        while cur:
            height += 1
            cur = cur.left

        start, end = 0, 2 ** (height - 1) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if self.is_valid_leaf(mid, root, height):
                start = mid
            else:
                end = mid

        if self.is_valid_leaf(end, root, height):
            return 2 ** (height - 1) + end

        return 2 ** (height - 1) + start

    def is_valid_leaf(self, index, root, height):
        s, e = 0, 2 ** (height - 1) - 1
        cur = root
        for i in range(height - 1):
            mid = s + (e - s) // 2
            if mid >= index:
                cur = cur.left
                e = mid
            else:
                cur = cur.right
                s = mid + 1

        return cur != None

print(1/3)