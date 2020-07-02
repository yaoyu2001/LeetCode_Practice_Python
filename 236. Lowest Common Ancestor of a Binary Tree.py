# Definition for a binary tree node.
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path = []
        self.path_p = []
        self.path_q = []

        self.finish = 0

        self.preorder(root, p, self.path,self.path_p,self.finish, 0)
        print(self.path_p)
        self.path.clear()
        self.finish = 0
        self.preorder(root, q, self.path, self.path_q, self.finish,1)
        print(self.path_q)

        result = -1

        p_len,q_len = len(self.path_p),len(self.path_q)
        if p_len<q_len:
            for counter in range(p_len):
                if self.path_p[counter] == self.path_q [counter]:
                    result = self.path_p[counter]
        else:
            for counter in range(q_len):
                if self.path_p[counter] == self.path_q [counter]:
                    result = self.path_p[counter]
        return result.val


    def preorder(self,node, search, path, result, finish, pq):
        """Node = current node, search = a node need to search, path: a stack to save path"""
        """result = final path, finish: a mark to indicate if we have found target node"""
        if not node or self.finish == 1:
            """Find target or reach to leave node, return"""
            return
        if pq == 0:
            self.path_p.append(node)
        else:
            self.path_q.append(node)

        """Push the current node to stack when pre-order traversal"""
        if node == search:
            self.finish = 1


        self.preorder(node.left, search, path, result, finish, pq) # Traversal left child
        self.preorder(node.right, search, path, result, finish, pq) # Traversal right child

        if pq == 0 and self.finish == 0:
            self.path_p.pop()
        elif pq == 1 and self.finish == 0:
            self.path_q.pop()
        # pop node from path when finish traversal
        # print("1")

a = TreeNode(3)

b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(7)
e = TreeNode(8)
f = TreeNode(9)
g = TreeNode(10)

a.left =b
a.right = c
b.left = d
b.right = e
d.left = f
d.right = g

so = Solution()

# print(so.lowestCommonAncestor(a,b,c))
print(a.left.val)
aa = copy.deepcopy(a)
print(aa.left.val)

print(a == aa)
a1 = 1
b1 = 1
print(a1 == b1)
print(id(a),id(b))
print(a.left.left)
print(aa.left.left)
print(a.left.left.val)
print(aa.left.left.val)

t1 = 1
t2 = '1'
t3 = t1*1
t4 = t1*t1
t5 = 2
print(t1 == t2)
print(t1 == t3)
print(t1 is t3)
print(t1 is t4)

print(id(t1),id(t3),id(t4))
t1 +=1
print("t1 is t5")
print(t1 is t5)
print(id(t1),id(t3))
t1 +=1
print(id(t1),id(t3))

# s1 = "a"
# s2 = "a"
# print(s1 is s2)
# print(id(s1),id(s2))
# t1 +="a"
# print(id(s1),id(s2))
s1 = 'abc'
print(s1.index("b"))

str1 = "a"
print(id(str1))
print(id(str1.upper()))