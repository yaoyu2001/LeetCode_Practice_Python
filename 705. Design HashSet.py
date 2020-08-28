class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, newValue):
        if not self.exists(newValue):
            new_node = Node(newValue, self.head.next)
            self.head.next = new_node

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.val == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)



    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)