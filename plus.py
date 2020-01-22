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