# Definition for singly-linked list.
# https://www.youtube.com/watch?v=sd9gE4_Dntk&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=2&t=2883s
# Fast and slow pointer
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        meet = None

        while fast:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return None
            fast = fast.next
            if fast == slow:
                meet = fast
                break
        # For A list node which has loop 1>2>3>4>5>6>7>3 a:2>3 b: 4>5>6  c:7>3 they meet at 6 ,the end of b
        # Because fast pointer's speed is twice as slow, so slow = a + b fast = a + b + c + b so 2slow = fast , 2a + 2b = a + b + c + b so a = c
        # So begin from head and meet, while these two pointer meet, it's the begin of loop
        if meet == None:
            return None
        while head and meet:
            if head == meet:
                return head
            head = head.next
            meet = meet.next

        return None
