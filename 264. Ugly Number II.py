import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        factors = [2, 3, 5]
        seen = {2, 3, 5}
        pq = []
        # Use a heap to store ugly numbers
        # First push all basic prime factors
        for item in factors:
            heapq.heappush(pq, item)

        for i in range(n - 1):
            # Out put the k-1 th element, because eles start from 2
            temp = heapq.heappop(pq)
            result = temp
            # New elements added, which equals to the smallest element k * 2 ,3 and 5
            for item in factors:
                new_ugly = temp * item
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(pq, new_ugly)

        return result