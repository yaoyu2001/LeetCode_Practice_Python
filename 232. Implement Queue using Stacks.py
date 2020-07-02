class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_push, self.stack_pop = [], []

    def push_to_pop(self):
        if len(self.stack_pop) == 0:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_push.append(x)
        self.push_to_pop()

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack_pop) == 0 and len(self.stack_push) == 0:
            return
        self.push_to_pop()
        return self.stack_pop.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack_pop) == 0 and len(self.stack_push) == 0:
            return
        self.push_to_pop()
        return self.stack_pop[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_pop) == 0 and len(self.stack_push) == 0:
            return True
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.peek())
print(obj.pop())
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()