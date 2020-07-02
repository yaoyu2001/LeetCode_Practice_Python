import collections
# https://www.youtube.com/watch?v=NDpwj0VWz1U&t=1s

class DlinkedNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.capacity = capacity
        # self.cache = {}
        self.cache = collections.defaultdict(DlinkedNode)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        res = -1
        node = self.cache.get(key, None)
        if node is not None:
            res = node.value
            self.removeNode(node)
            self.addNode(node)
        return res

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if node is not None:
            self.removeNode(node)
            node.value = value
            self.addNode(node)


        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.prev.key]
                self.removeNode(self.tail.prev)

            new_node = DlinkedNode()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            self.addNode(new_node)

    def addNode(self, node: DlinkedNode):
        head_next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next = head_next
        head_next.prev = node

    def removeNode(self, node: DlinkedNode):

        next_node = node.next
        prev_node = node.prev

        next_node.prev = prev_node
        prev_node.next = next_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)