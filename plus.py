# print(2 % 3)
from collections import deque

data = deque()

data.append(1)
data.append(2)
# data.append(3)
print(data)
data.rotate(1)
print(data)
data.append(3)
print(data)
data.rotate(-2)
print(data)
# data.popleft()
print(data.popleft())
a = "abbbbc"
b = "bc"
print(a.index(b))


s1 = 'abc'
s2 = s1

print(s2)
s1 = 'abcd'
print(s2)

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
        self.visit = 0

    def run(self):
        self.push(self.visit)

    def push(self, visit):
        self.visit += 1

t = GraphNode(1)
print(t.visit)
t.run()
print(t.visit)
