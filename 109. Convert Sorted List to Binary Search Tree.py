# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        arr = self.convertToList(head)

        def inOrder(left, right):
            if left>right:
                return None

            mid = (left + right) // 2
            node = TreeNode(arr[mid])
            if left == right:
                return node
            node.left = inOrder(left, mid-1)
            node.right = inOrder(mid + 1, right)

            return node



    def findsize(self,head:ListNode):
        idx = 0
        while head:
            idx += 1
            head = head.next

        return idx

    def convertToList(self,head):
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res

print(5//2)