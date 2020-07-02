import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        s = set([2,3,5])
        visited = {2,3,5}
        pq = [2,3,5]
        heapq.heapify(pq)
        result = 1
        for i in range(n - 1):
            temp = heapq.heappop(pq)
            result = temp
            for item in s:
                new = temp * item
                if new not in visited:
                    visited.add(new)
                    heapq.heappush(pq, new)
        return result
