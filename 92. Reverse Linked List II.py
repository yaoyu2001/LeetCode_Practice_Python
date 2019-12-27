
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



def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    change_len = n - m + 1  # calculate number of nodes need to reverse
    pre_head = None  # Define the node before start node
    result = head  # The head node after reverse
    while head and m > 1:
        pre_head = head   # previous node
        head = head.next  # move forward m-1 position to get head node
        m -= 1

    modify_list_tail = head  # The tail after reverse, namely the current head

    new_head = None  # The first node after reverse
    while head and change_len:
        next = head.next
        head.next = new_head
        new_head = head
        head = next
        change_len -= 1  # minus 1 after completed one reverse

    modify_list_tail.next = head  # connect the tail of list node after reverse and the first node that after reverse area

    if pre_head:  # if pre_head not equal to None, that means reverse area not from the first node
        pre_head.next = new_head
    else:
        """That means reverse from first node, now the result equal to the first node after reverse, is new_head"""
        result = new_head
    return result

# print(reverseBetween(a,2,5).val)

def print_ListNode(head):
    while head:
        print(head.val)
        head = head.next

print_ListNode(a)
print("******")
print_ListNode(reverseBetween(a,2,4))