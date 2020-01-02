def strangeSort(mapping, nums):
    maps = [0] * 10
    for i, v in enumerate(mapping):
        maps[v] = i
    ans = sorted([int("".join([str(maps[int(i)]) for i in v])), i, v] for i, v in enumerate(nums))

    res = sorted([["".join([str(maps[int(i)]) for i in v]),i,v] for i, v in enumerate(nums)])
    print(res)
    return [ans_[-1] for ans_ in ans]


mapping = [3,5,4,6,2,7,9,8,0,1]
nums = ['990', '332', '32','880','0880','6']

print(strangeSort(mapping,nums))