# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(10)
b = ListNode(20)
c = ListNode(30)
d = ListNode(40)
e = ListNode(50)

a.next = b
b.next = c
c.next = d
d.next = e


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
        return new_head