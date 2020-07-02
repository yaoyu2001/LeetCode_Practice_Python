# 00000-00111-01000-01011
# 00000 - 00111- 00100
def FinalProblem( str:str):
    res = 0
    meet_one = False
    for item in str:
        if not meet_one:
            if item =="1":
                meet_one = True
        else:
            if item =="0":
                res += 2
                meet_one = False

    if meet_one == True:
        res += 1
    return res

print(FinalProblem("011001101"))
print(FinalProblem("00101"))

