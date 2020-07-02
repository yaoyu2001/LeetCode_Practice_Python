class Solution:
    def reconstructQueue(self, people: [[int]]) ->[[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        res = []

        for height, pre_people in people:
            res.insert(pre_people, [height, pre_people])

        return res