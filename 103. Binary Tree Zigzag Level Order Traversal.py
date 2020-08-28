# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter, Use None as delimiter
        node_queue = deque([root, None])

        # First level from left to right
        is_order_left = True

        while node_queue:
            curr_node = node_queue.popleft()

            # If curr_node is not none, means traversal still in the same level
            if curr_node:
                # From left to right, append from right
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)
                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # Finish one level
                ret.append(level_list)
                # Add a delimiter for next level
                if len(node_queue)>0:
                    node_queue.append(None)

                # Next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret