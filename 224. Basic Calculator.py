# https://www.youtube.com/watch?v=Rp_qRZ6TTg0&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=3&t=1573s
# https://www.youtube.com/watch?v=Rp_qRZ6TTg0&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=3&t=1573s
class Solution:
    def calculate(self, s: str) -> int:

        def compute(number_stack: [], operation_stack):
            if len(number_stack) < 2:
                """Special value like (12345)"""
                return
            num2 = number_stack[-1]
            number_stack.pop()
            num1 = number_stack[-1]
            number_stack.pop()
            if operation_stack[-1] == '+':
                number_stack.append(num1 + num2)
            elif operation_stack[-1] == '-':
                number_stack.append(num1 - num2)
            operation_stack.pop()

        _STATE_BEGIN = 0
        _NUMBER_STATE = 1
        _OPERATION_STATE = 2

        number_stack,operation_stack = [],[]
        number = 0

        state = _STATE_BEGIN
        computer_flag = 0
        i = 0
        while i < len(s):


            if s[i] == ' ':
                i+=1
                continue
            if state == _STATE_BEGIN:
                if ord('0')<= ord(s[i])<= ord('9'):
                    state = _NUMBER_STATE
                else:
                    state = _OPERATION_STATE
                i -= 1

            elif state == _NUMBER_STATE:
                if ord('0') <= ord(s[i]) <= ord('9'):
                    number = 10*number + (ord(s[i]) - ord("0"))
                else:
                    number_stack.append(number)
                    if computer_flag == 1:
                        compute(number_stack, operation_stack)
                    number = 0
                    i -= 1
                    state = _OPERATION_STATE

            elif state == _OPERATION_STATE:
                if s[i] == '+' or s[i] == '-':
                    operation_stack.append(s[i])
                    computer_flag = 1
                elif s[i] == '(':
                    computer_flag = 0
                elif ord('0') <= ord(s[i]) <= ord('9'):
                    state = _NUMBER_STATE
                    i -= 1
                elif s[i] == ')':
                    compute(number_stack,operation_stack)
            i+=1
        if number!= 0:
            number_stack.append(number)
            compute(number_stack, operation_stack)
        if number == 0 and len(number_stack) == 0:
            return 0

        return number_stack[0]




so = Solution()

print(so.calculate("(1+(4+5+2)-3)+(6+8)"))
