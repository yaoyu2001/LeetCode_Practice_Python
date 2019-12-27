# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_set = set()
        while headA:
            node_set.add(headA)
            headA = headA.next
        while headB:
            if headB in node_set:
                return headB
            headB = headB.next

        return None

    # Method 2 O(1) Space complexity compare length of two list node
    def get_list_length(self, head: ListNode):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # Move the point of long list node  and  short list node to the same position
    def forward_long_list(self, long_len, short_len, head):
        delta = long_len - short_len
        while head and delta:
            head = head.next
            delta -= 1
        return head

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        list_A_len = self.get_list_length(headA)
        list_B_len = self.get_list_length(headB)

        if list_A_len > list_B_len:
            headA = self.forward_long_list(list_A_len, list_B_len, headA)
        else:
            headB = self.forward_long_list(list_B_len, list_A_len, headB)
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


s = Solution

a = ListNode(10)
b = ListNode(20)
c = ListNode(30)
d = ListNode(40)
e = ListNode(50)

a.next = b
b.next = c
c.next = d
d.next = e

print(s.getIntersectionNode(None, a, b).val)
