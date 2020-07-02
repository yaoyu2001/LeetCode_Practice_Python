# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: [int]) -> bool:

        def check_vaild(node, arr, index):
            if node is None or index == len(arr):
                return False

            if node.left is None and node.right is None and node.val == arr[index] and index == len(arr) - 1:
                return True

            return node.val == arr[index] and check_vaild(node.left, arr, index+1) or check_vaild(node.right, arr, index+1)

        index = 0
        return check_vaild(root, arr, index)