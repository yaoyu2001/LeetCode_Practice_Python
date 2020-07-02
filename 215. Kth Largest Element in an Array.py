import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pqueue = list()

        for item in nums:
            if len(pqueue) < k:
                heapq.heappush(pqueue, item)
            elif pqueue[0] < item:
                heapq.heappop(pqueue)
                heapq.heappush(pqueue, item)


        return pqueue[0]

nums = [3,2,1,5,6,4]

k = 4
so = Solution()
print(so.findKthLargest(nums, 2))