from queue import PriorityQueue as PQueue
class Solution:
    def trapRainWater(self, heightMap: [[int]]) -> int:
        pq = PQueue()
        set_ = [[1,1,2], [2,1,3], [1,3,1]]
        for item in set_:
            pq.put([item])
        set_str = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        pq_str = PQueue()
        for item in set_str:
            pq_str.put(item)

        # print(pq.queue)
        print(pq_str.queue)

        while pq:
            # print(pq.get()[1])
            print(pq_str.get())

so = Solution()
so.trapRainWater([[1]])

# try:
#     import Queue as Q  # ver. < 3.0
# except ImportError:
#     import queue as Q

class Skill:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print ('New Level:', description)

    def __lt__(self, other):
        if self.priority <= other.priority:
            return True
        else:
            return False

q = PQueue()

q.put(Skill(5, 'Proficient'))
q.put(Skill(10, 'Expert'))
q.put(Skill(1, 'Novice'))

while not q.empty():
    next_level = q.get()
    # print ('Processing level:', next_level.description)