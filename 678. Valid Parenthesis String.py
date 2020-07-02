class Solution(object):
    def checkValidString(self, s):
        low, high = 0, 0  # The lowest and highest Possibly numbers of "(" we have

        for c in  s:
            low += 1 if c == "(" else -1
            high += 1 if c !=")" else -1
            if high<0:
                break
            low = max(low, 0)
        return low == 0

