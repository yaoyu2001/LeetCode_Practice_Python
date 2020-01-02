class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummyHead = ListNode(None)
    p = l1
    q = l2
    curr = dummyHead
    carry = 0
    while p or q:
        x = p.val if p is not None else 0
        y = q.val if q is not None else 0

        sum = carry + x + y
        carry = sum //10
        curr.next = ListNode(sum%10)

        if p:
            p = p.next
        if q:
            q = q.next
    if carry > 0:
        curr.next = ListNode(carry)

    return dummyHead.next


# print(int(11/10))