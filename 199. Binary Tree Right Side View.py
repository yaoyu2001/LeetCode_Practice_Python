# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        view = []
        q = deque()

        if root:
            q.append([root, 0])

        while q:
            temp = q.popleft()
            node = temp[0]
            depth = temp[1]

            if len(view) == depth:
                view.append(node.val)
            else:
                view[depth] = node.val

            if node.left:
                q.append([node.left, depth+1])
            if node.right:
                q.append([node.right, depth + 1])

        return view