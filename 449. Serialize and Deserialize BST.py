# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def __init__(self):
        self.code = ""
        self.collect_nodes = []

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.code = ""
        self.code_tree(root)
        return self.code



    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        self.decode_tree()
        for i in range(1, len(self.collect_nodes)):
            self.insert(self.collect_nodes[0], self.collect_nodes[i])

        return self.collect_nodes[0]


    def code_tree(self, node):
        if not node:
            return
        self.code += str(node.val) + "#"
        self.code_tree(node.left)
        self.code_tree(node.right)

    def decode_tree(self):

        val = 0
        for i in range(len(self.code)):
            if self.code[i] == '#':
                node = TreeNode(val)
                self.collect_nodes.append(node)
                val = 0
            else:
                val = val*10 + int(self.code[i])

    def insert(self,node, insert_node):

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

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))