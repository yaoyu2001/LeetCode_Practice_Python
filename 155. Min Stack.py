

# Method 1
# compare value

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_data = []
        self.stack_min = []

    def push(self, x: int) -> None:
        if len(self.stack_min) == 0:
            self.stack_min.append(x)
        elif x <= self.getMin():
            self.stack_min.append(x)

        self.stack_data.append(x)



    def pop(self) -> None:
        if len(self.stack_data) == 0 :return
        value = self.stack_data[-1]
        if value == self.getMin():
            self.stack_min.pop()
        return value
    def top(self) -> int:
        return self.stack_data[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Method 2 when push, if x > min, push min again.
class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_data = []
        self.stack_min = []

    def push(self, x: int) -> None:
        if len(self.stack_min) == 0:
            self.stack_min.append(x)
        elif x <= self.getMin():
            self.stack_min.append(x)
        else:
            self.stack_min.append(self.stack_min[-1])

        self.stack_data.append(x)



    def pop(self) -> None:
        if len(self.stack_data) == 0 : return
        self.stack_min.pop()
        return self.stack_data.pop()

    def top(self) -> int:
        return self.stack_data[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]