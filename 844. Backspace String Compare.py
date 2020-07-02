class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.changestr(S) == self.changestr(T)

    def changestr(self, arr):
        res = ""
        for item in arr:
            if item != "#":
                res += item
            else:
                res = res[:-1]
        return res