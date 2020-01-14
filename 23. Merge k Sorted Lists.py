# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# https://www.youtube.com/watch?v=sd9gE4_Dntk&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=2&t=7922s



# Definition for singly-linked list.
# Sort implement
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        node_vec = list()
        for head in lists:
            while head:
                node_vec.append(head)
                head = head.next
        if len(node_vec) == 0: return None
        node_vec.sort(key=lambda x:x.val)
        for i in range(1, len(node_vec)):
            node_vec[i-1].next = node_vec[i]

        node_vec[len(node_vec) -1].next = None
        return node_vec[0]


    def compare(self,list_a :ListNode, list_b : ListNode):
        return list_a.val > list_b.val

# Divide-and-conquer algorithm
class Solution2:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            return self.mergeTwoLists(lists[0],lists[1])

        mid = len(lists) // 2

        sub1_lists,sub2_lists = list(),list()
        for i in range(0,mid):
            sub1_lists.append(lists[i])
        for j in range(mid, len(lists)):
            sub2_lists.append(lists[j])

        l1 = self.mergeKLists(sub1_lists)
        l2 = self.mergeKLists(sub2_lists)

        return self.mergeTwoLists(l1,l2)



    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy
        while l1 and l2:
            if l1.val<l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return dummy.next