from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # Append to the end and then rotate to the left
        # so that the appended element comes at the top.
        self._data.append(x)
        self._data.rotate(-(len(self._data) - 1))

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._data.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._data[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._data) == 0