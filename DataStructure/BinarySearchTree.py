class BianryTreeNode:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None


class BianrySearchTree:
    def __init__(self):
        self.root = BianryTreeNode(None)
        self.collect_nodes = []
        self.code = ""

    def insert(self,node:BianryTreeNode, insert_node: BianryTreeNode):

        if insert_node.data < node.data:
            if node.left:
                self.insert(node.left, insert_node)
            else:
                node.left = insert_node
        else:
            if node.right:
                self.insert(node.right, insert_node)
            else:
                node.right = insert_node

    def preorder_print(self, node, layer):
        if not node:
            return

        print(f"{layer}layer")
        print(node.data)
        self.collect_nodes.append(node)
        self.code += str(node.data) + "#"
        self.preorder_print(node.left, layer + 1)
        self.preorder_print(node.right, layer + 1)

    def search(self, node, value):
        if node.data == value:
            return True

        if value < node.data:
            if node.left:
                return self.search(node.left, value)
            else:
                return False
        else:
            if node.right:
                return self.search(node.right, value)
            else:
                return False

    def rebuild(self):
        for node in self.collect_nodes:  # Eliminate pointer
            node.left = None
            node.right = None

        for i in range(1, len(self.collect_nodes)):
            self.insert(self.collect_nodes[0], self.collect_nodes[i])

        print("Rebuild")
        self.preorder_print(self.collect_nodes[0], 0)

    def decode(self):

        val = 0
        for i in range(len(self.code)):
            if self.code[i] == '#':
                print(f"Val is {val}")
                val = 0
            else:
                val = val*10 + int(self.code[i])


a = BianryTreeNode(8)
b = BianryTreeNode(3)
c = BianryTreeNode(10)
d = BianryTreeNode(1)
e = BianryTreeNode(6)
f = BianryTreeNode(15)
g = BianryTreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

so = BianrySearchTree()
so.insert(a,g)

so.preorder_print(a,0)

# print(so.search(a, 5))
# # print(so.search(a, 11))
# # print(so.collect_nodes)
# so.rebuild()

print(so.code)
so.decode()