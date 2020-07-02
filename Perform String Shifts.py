class Solution:
    def stringShift(self, s: str, shift: [[int]]) -> str:
        shift_distance = 0
        step = 0

        for st in shift:
            if st[0] == 1:
                s = s[-st[1]:] + s[:-st[1]]
            else:
                s = s[st[1]:] + s[:st[1]]

        #     if st[0] == 0:
        #         shift_distance -= 1
        #         step -= st[1]
        #     else:
        #         shift_distance += 1
        #         step += st[1]
        #
        # print(f"step:{step}")
        # step = step % len(s)
        # if step < 0:
        #     s = s[-step:] + s[:-step]
        # elif step > 0:
        #     s = s[len(s) - step:] + s[:len(s) - step]

        return s

so = Solution()
str = "xqgwkiqpif"
shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]

print(so.stringShift(str,shift))

print(str[-4:]+str[:-4])
str = str[-4:]+str[:-4]
print(str[7:]+str[:7])