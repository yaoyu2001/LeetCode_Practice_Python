# Definition for a binary tree node.
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:


        def preOrder(node, sum, path_value=0, path=[],result=[]):
            if root is None:
                return
            path_value += root.val
            path.append(root.val)
            if not root.left and not root.right and path_value == sum:
                result.append(copy.deepcopy(path))

            preOrder(root.left,sum,path_value,path,result)
            preOrder(root.right,sum,path_value,path,result)
            path_value -= root.val
            path.pop()

        result = preOrder(root, sum)
        return result