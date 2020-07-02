# https://www.youtube.com/watch?v=cyGTFYJZY_E&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=5&t=2293s
class Solution:
    def __init__(self):
        self.result = []
        self.left, self.right = 0,0

    def generateParenthesis(self, n: int) -> [str]:

        self.left, self.right = n,n
        self.generate("", self.left, self.right)

        return self.result

    def generate(self,item,left,right):
        if  left == 0 and right == 0:
            self.result.append(item)
            return
        if left > 0:
            self.generate(item + "(", left-1,right)
        if left < right:
            self.generate(item + ")", left, right - 1)


so = Solution()
# so.generate("",2,2,2)
# print(len(so.result))
# print(so.result)
print(so.generateParenthesis(2))