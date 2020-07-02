# http://poj.org/problem?id=1363
from collections import deque
class Solution:
    def check_is_valid_order(self, input):
        order = deque(input)
        stack = []
        for i in range(1, len(order)+1):
            stack.append(i)
            while len(stack) !=0 and order[0]==stack[-1]:
                stack.pop()
                order.popleft()

        if len(stack) != 0:
            return False
        return True

input = [3,2,5,4,1]
so = Solution()
print(so.check_is_valid_order(input))