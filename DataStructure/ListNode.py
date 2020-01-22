
class ListNode:
    def __init__(self, val):
        self.val = val
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

def print_ListNode(head):
    while head:
        print(head.val)
        head = head.next


# print_ListNode(a)

# Reverse Linked List
# def reverse_listnode(head):
#     s = list()
#     while head:
#         s.append(head)
#         head = head.next
#
#     res = s.pop()
#     temp = res
#     while s:
#         temp.next = s.pop()
#         temp = temp.next
#     temp.next = None
#     return res

def reverse_listnode(head):
    new_head = None
    while head:
        temp = head.next
        head.next = new_head
        new_head = head
        head = temp
    return new_head

a_ = reverse_listnode(a)

print_ListNode(a_)