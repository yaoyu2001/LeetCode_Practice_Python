# 1 Recursive
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}
    def copyRandomList(self,head):

        if head == None:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        node = Node(head.val, None, None)

        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

a = Node(1,None,None)
b = Node(2,None,None)
c = Node(3,None,None)
a.random = c
a.next = b
b.next = c
b.random = a

s = Solution()
s.copyRandomList(a)

# Method 2 O（n）
class Solution2(object):
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None,None)
                return self.visited[node]

        return None

    def copyRandomList(self, head):
        if not head:
            return head

        old_node = head

        new_node = Node(old_node.val, None, None)

        self.visited[old_node] = new_node

        while old_node:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

s2 =Solution2()
node_2 = s2.copyRandomList(a)

print(node_2.val)
print(node_2.random.val)
print(node_2.next.val)