
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # None case
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pesudoHead = Node(None, None, head, None)

        self.flatten_dsf(pesudoHead, head)
        # detach the pseudo head from the real head
        pesudoHead.next.prev = None
        return pesudoHead.next

    # Dsf to return tail of the flatten list
    def flatten_dsf(self, prev, cur):
        if not cur:
            return prev

        cur.prev = prev
        prev.next = cur

        # Use a temp variable to store next node, so that connect tail and that next node
        temp_next = cur.next
        # Recursion to get child as tail, and let current node's child = None
        # If a node don't have tail, tail will equal to current node
        tail = self.flatten_dsf(cur, cur.child)
        cur.child = None
        # Recursion to flat current node and next node, then jump to next node
        return self.flatten_dsf(tail, temp_next)

