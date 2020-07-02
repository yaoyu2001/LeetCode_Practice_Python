# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tree_s = self.preorder(s, True)
        tree_t = self.preorder(t, True)
        return tree_t in tree_s


    def preorder(self, tree, if_left):
        if tree == None:
            if if_left:
                return "left_null"
            else:
                return "right_null"
        return "#" + str(tree.val) + " " + self.preorder(tree.left, True) + " " + self.preorder(tree.right, False)