# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#  Method 1 : Set
def hasCycle(head: ListNode) -> bool:
    node_set = set()
    while head:
        if head in node_set:
            return head
        node_set.add(head)
        head = head.next
    return None


#  Method 2 : Fast and slow point
def detectCycle(head):
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

    if meet == None:
        return None
    while head and meet:
        if head == meet:
            return head
        head = head.next
        meet = meet.next

    return None
