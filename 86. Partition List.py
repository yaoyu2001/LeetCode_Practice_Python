# https://www.youtube.com/watch?v=sd9gE4_Dntk&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=2&t=3198s
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next

a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

k = 3

s = Solution()
print(s.partition(a, k).val)