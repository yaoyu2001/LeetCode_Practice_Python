class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:

            if c == "(" or c == "[" or c == "{":
                stack.append(c)

            elif c == ")":
                temp = stack.pop() if stack else None
                if temp != "(":
                    return False
            elif c == "]":
                temp = stack.pop() if stack else None
                if temp != "[":
                    return False
            elif c == "}":
                temp = stack.pop() if stack else None
                if temp != "{":
                    return False

        if len(stack) == 0:
            return True

        return False