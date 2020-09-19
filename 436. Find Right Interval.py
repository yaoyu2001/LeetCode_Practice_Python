import collections
class Solution:
    def findRightInterval(self, intervals: [[int]]) -> [int]:
        start = collections.defaultdict(int)
        for i, num in enumerate(intervals):
            start[num[0]] = i

        print(start)
        res = [-1] * len(intervals)

        for i, num in enumerate(intervals):
            for j in start.keys():
                print(j)
                if j >= num[1]:
                    res[i] = start[j]

        return res

so  = Solution()

print(so.findRightInterval([[1,2],[2,3],[0,1],[3,4]]))
