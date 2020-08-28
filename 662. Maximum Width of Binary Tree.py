# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0

        # Use a queue to store a pair that indicate a node and it's index
        # For a full binary tree, if a node's index is c, the left and right node of this node is 2*c and 2*c + 1
        queue = collections.deque()
        queue.append((root, 0))

        # BFS
        while queue:
            level_length = len(queue)
            val, level_head_index = queue[0]

            for i in range(level_length):
                node, col_index = queue.popleft()
                # Append nodes in next level to queue
                if node.left:
                    queue.append((node.left, 2*col_index))
                if node.right:
                    queue.append((node.right, 2*col_index + 1))

            max_width = max(max_width, col_index - level_head_index + 1)

        return max_width
